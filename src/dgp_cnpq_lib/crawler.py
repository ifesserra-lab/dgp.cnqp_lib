from playwright.sync_api import sync_playwright
import json
import time
import unicodedata
import re

def extract_text(element, selector):
    el = element.query_selector(selector)
    return el.inner_text().strip() if el else ""

def normalize_key(text):
    # Remove accents and convert to snake_case
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', '_', text)
    return text

def clean_value(value):
    if not value:
        return ""
    # Remove excessive whitespace
    value = re.sub(r'\s+', ' ', value).strip()
    return value

def extract_table(table):
    headers = [normalize_key(th.inner_text().strip()) for th in table.query_selector_all('th')]
    
    # Remove "acoes" column if present
    if "acoes" in headers:
        action_idx = headers.index("acoes")
        del headers[action_idx]
    else:
        action_idx = -1
        
    rows = []
    for tr in table.query_selector_all('tr')[1:]:  # Skip header
        cells = [td.inner_text().strip() for td in tr.query_selector_all('td')]
        if not cells: 
            continue
            
        # Check for empty record message
        if len(cells) == 1 and "Nenhum registro" in cells[0]:
            continue

        if action_idx != -1 and len(cells) > action_idx:
            del cells[action_idx]
            
        if len(headers) == len(cells):
            row = dict(zip(headers, cells))
            
            # Clean values in the row and handle specific period fields
            cleaned_row = {}
            for k, v in row.items():
                val = clean_value(v)
                
                # Check for "De ... a ..." pattern in participation period
                if "periodo" in k and val.lower().startswith("de ") and " a " in val.lower():
                    # Pattern: "De 21/04/2015 a 18/09/2017"
                    match = re.search(r'de\s+(.*?)\s+a\s+(.*)', val, re.IGNORECASE)
                    if match:
                        cleaned_row['data_inicio'] = match.group(1)
                        cleaned_row['data_fim'] = match.group(2)
                    else:
                        cleaned_row[k] = val
                else:
                    cleaned_row[k] = val
            
            rows.append(cleaned_row)
            
    return rows

def parse_fieldset(fieldset):
    legend = extract_text(fieldset, 'legend')
    data = {}
    
    # Extract key-value pairs
    labels = fieldset.query_selector_all('label.control-label')
    for label in labels:
        raw_key = label.inner_text().strip()
        key = normalize_key(raw_key.replace(':', ''))
        
        # Get value
        parent = label.evaluate_handle('el => el.parentElement')
        full_text = parent.inner_text().strip()
        # Remove the label text from the full text to get value
        val_text = full_text.replace(raw_key, '', 1).strip()
        
        # Specific handling for known fields
        if key == "lideres_do_grupo":
             # Split by newline or multiple spaces if names are joined
             data[key] = [clean_value(v) for v in val_text.split('\n') if v.strip()]
        else:
             data[key] = clean_value(val_text)

    # Extract tables with heuristic for naming
    tables = fieldset.query_selector_all('table')
    if tables:
        # If specific section like Human Resources, try to key by the first column header of each table
        # which usually describes the category (Pesquisadores, Estudantes)
        extracted_tables = {}
        generic_tables = []
        
        for t in tables:
            rows = extract_table(t)
            if not rows: continue
            
            # Try to infer a key from the first key of the first row
            # e.g. if row is {'pesquisadores': 'Name', ...} use 'pesquisadores'
            first_key = list(rows[0].keys())[0] if rows and rows[0] else None
            
            if legend and "recursos humanos" in legend.lower() and first_key:
                 extracted_tables[first_key] = rows
            elif legend and "linhas de pesquisa" in legend.lower():
                 # For research lines, it's just a list of lines
                 generic_tables.extend(rows)
            else:
                 generic_tables.append(rows)
        
        if extracted_tables:
            data.update(extracted_tables)
        if generic_tables:
            # If it's just one list, don't nest it
            if len(generic_tables) == 1 and isinstance(generic_tables[0], dict) == False: 
                 # Wait, generic_tables is list of lists of dicts (from multiple tables)
                 # If we have only one table's data which is a list of dicts, assign it directly
                 # But valid for extracting all rows from all tables if they mean the same thing
                 # For "linhas de pesquisa", we extended.
                 data['items'] = generic_tables
            elif normalize_key(legend) == "linhas_de_pesquisa":
                 data['linhas'] = generic_tables
            else:
                 data['outros_dados'] = generic_tables

    # Text content (Repercussões)
    if not labels and not tables: # logic reuse
        paragraphs = fieldset.query_selector_all('p')
        if paragraphs:
             text = "\n".join([p.inner_text().strip() for p in paragraphs])
             if text: data['descricao'] = clean_value(text)
        else:
             # Fallback
             cloned_text = fieldset.evaluate('''el => {
                const clone = el.cloneNode(true);
                const toRemove = clone.querySelectorAll('legend, table');
                toRemove.forEach(e => e.remove());
                return clone.innerText.trim();
             }''')
             if cloned_text:
                 data['descricao'] = clean_value(cloned_text)
        
    return legend, data

def crawl_cnpq_group(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        print(f"Navigating to {url}...")
        page.goto(url)
        
        # Wait for content to load
        page.wait_for_selector('fieldset', timeout=10000)
        
        # Just in case, scroll down
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1) 
        
        result = {}
        
        fieldsets = page.query_selector_all('fieldset')
        for fs in fieldsets:
            legend, content = parse_fieldset(fs)
            if legend:
                key = normalize_key(legend)
                # Clean up empty sub-structures
                if 'outros_dados' in content and not content['outros_dados']:
                    del content['outros_dados']
                
                # If content is just one key "items" or "descricao", maybe flatten?
                # Keeping it structured under the section key is improved enough.
                result[key] = content
            
        browser.close()
        return result

if __name__ == "__main__":
    target_url = "http://dgp.cnpq.br/dgp/espelhogrupo/4201359100034312"
    data = crawl_cnpq_group(target_url)
    
    output_file = "grupo_pesquisa.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Data saved to {output_file}")
