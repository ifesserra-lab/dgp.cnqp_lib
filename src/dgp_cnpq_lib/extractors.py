import re
import unicodedata
from typing import Any, Dict, List, Tuple

from playwright.sync_api import ElementHandle


class BaseExtractor:
    @staticmethod
    def extract_text(element: ElementHandle, selector: str) -> str:
        """Extracts text from an element matching the selector."""
        if not element:
            return ""
        el = element.query_selector(selector)
        return el.inner_text().strip() if el else ""

    @staticmethod
    def normalize_key(text: str) -> str:
        """Normalizes a string to be used as a dictionary key (snake_case)."""
        text = text.strip()
        text = unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("ASCII")
        text = text.lower()
        text = re.sub(r"[^\w\s]", "", text)
        text = re.sub(r"\s+", "_", text)
        return text

    @staticmethod
    def clean_value(value: str) -> str:
        """Cleans a string value by removing excessive whitespace."""
        if not value:
            return ""
        return re.sub(r"\s+", " ", value).strip()


class TableExtractor(BaseExtractor):
    def extract(self, table: ElementHandle) -> List[Dict[str, str]]:
        """Extracts data from a table element."""
        headers = [
            self.normalize_key(th.inner_text().strip()) for th in table.query_selector_all("th")
        ]

        # Remove "acoes" column if present
        if "acoes" in headers:
            action_idx = headers.index("acoes")
            del headers[action_idx]
        else:
            action_idx = -1

        rows = []
        # Skip header
        for tr in table.query_selector_all("tr")[1:]:
            cells = [td.inner_text().strip() for td in tr.query_selector_all("td")]
            if not cells:
                continue

            # Check for empty record message
            if len(cells) == 1 and "Nenhum registro" in cells[0]:
                continue

            if action_idx != -1 and len(cells) > action_idx:
                del cells[action_idx]

            if len(headers) == len(cells):
                row = dict(zip(headers, cells))
                rows.append(self._process_row(row))

        return rows

    def _process_row(self, row: Dict[str, str]) -> Dict[str, str]:
        """Cleans values in the row and handle specific period fields."""
        cleaned_row = {}
        for k, v in row.items():
            val = self.clean_value(v)

            # Check for "De ... a ..." pattern in participation period
            if "periodo" in k and val.lower().startswith("de ") and " a " in val.lower():
                match = re.search(r"de\s+(.*?)\s+a\s+(.*)", val, re.IGNORECASE)
                if match:
                    cleaned_row["data_inicio"] = match.group(1)
                    cleaned_row["data_fim"] = match.group(2)
                else:
                    cleaned_row[k] = val
                    if "data_inicio" not in cleaned_row:
                        cleaned_row["data_inicio"] = val  # Fallback
                    cleaned_row["data_fim"] = ""

            elif k == "data_inclusao":
                cleaned_row["data_inicio"] = val
                cleaned_row["data_fim"] = ""
            else:
                cleaned_row[k] = val

        # Post-cleanup: Ensure data_fim exists if data_inicio exists
        if "data_inicio" in cleaned_row and "data_fim" not in cleaned_row:
            cleaned_row["data_fim"] = ""

        return cleaned_row


class FieldsetParser(BaseExtractor):
    def __init__(self):
        self.table_extractor = TableExtractor()

    def parse(self, fieldset: ElementHandle) -> Tuple[str, Dict[str, Any]]:
        """Parses a fieldset element to extract legend and data."""
        legend = self.extract_text(fieldset, "legend")
        data = {}

        # Extract key-value pairs
        self._extract_labels(fieldset, data)

        # Extract tables
        self._extract_tables(fieldset, legend, data)

        # Text content (Repercussões) fallback
        if not data:
            self._extract_text_content(fieldset, data)

        return legend, data

    def _extract_labels(self, fieldset: ElementHandle, data: Dict[str, Any]):
        labels = fieldset.query_selector_all("label.control-label")
        for label in labels:
            raw_key = label.inner_text().strip()
            key = self.normalize_key(raw_key.replace(":", ""))

            # Get value
            parent = label.evaluate_handle("el => el.parentElement")
            full_text = parent.inner_text().strip()
            val_text = full_text.replace(raw_key, "", 1).strip()

            if key == "lideres_do_grupo":
                data[key] = [self.clean_value(v) for v in val_text.split("\n") if v.strip()]
            else:
                data[key] = self.clean_value(val_text)

    def _extract_tables(self, fieldset: ElementHandle, legend: str, data: Dict[str, Any]):
        all_tables = fieldset.query_selector_all("table")
        if not all_tables:
            return

        tables = []
        for t in all_tables:
            # IMPORTANT: Ensure the table belongs to THIS fieldset and not a nested one
            # compare the closest fieldset of the table with the current fieldset
            is_owned = fieldset.evaluate("(fs, t) => t.closest('fieldset') === fs", t)
            if is_owned:
                tables.append(t)

        if not tables:
            return

        extracted_tables = {}
        generic_tables = []

        for t in tables:
            rows = self.table_extractor.extract(t)
            if not rows:
                continue

            # Try to infer a key from the first key of the first row
            first_key = list(rows[0].keys())[0] if rows and rows[0] else None

            if first_key:
                # Check if it's an "Egresso" table
                # Active members have 'titulacao_maxima' (Pesquisadores)
                # or 'nivel_de_treinamento' (Estudantes)
                # Egressos have 'data_fim' (from 'periodo') and NO active indicators
                keys = rows[0].keys()
                is_active = "titulacao_maxima" in keys or "nivel_de_treinamento" in keys
                if "data_fim" in keys and not is_active:
                    first_key = f"egressos_{first_key}"

            if legend and "recursos humanos" in legend.lower() and first_key:
                extracted_tables[first_key] = rows
            elif legend and "linhas de pesquisa" in legend.lower():
                generic_tables.extend(rows)
            else:
                generic_tables.append(rows)

        if extracted_tables:
            data.update(extracted_tables)

        if generic_tables:
            if len(generic_tables) == 1 and not isinstance(generic_tables[0], dict):
                data["items"] = generic_tables
            elif self.normalize_key(legend) == "linhas_de_pesquisa":
                data["linhas"] = generic_tables
            else:
                data["outros_dados"] = generic_tables

    def _extract_text_content(self, fieldset: ElementHandle, data: Dict[str, Any]):
        paragraphs = fieldset.query_selector_all("p")
        if paragraphs:
            text = "\n".join([p.inner_text().strip() for p in paragraphs])
            if text:
                data["descricao"] = self.clean_value(text)
        else:
            cloned_text = fieldset.evaluate(
                """el => {
                const clone = el.cloneNode(true);
                const toRemove = clone.querySelectorAll('legend, table');
                toRemove.forEach(e => e.remove());
                return clone.innerText.trim();
             }"""
            )
            if cloned_text:
                data["descricao"] = self.clean_value(cloned_text)
