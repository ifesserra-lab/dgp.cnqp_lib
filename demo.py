import sys
from dgp_cnpq_lib import CnpqCrawler

def main():
    print("Iniciando demonstração do dgp_cnpq_lib...")

    # URL de exemplo (Espelho de Grupo)
    # Substitua por uma URL válida se necessário
    url = "http://dgp.cnpq.br/dgp/espelhogrupo/0225175815967657" 
    
    # 2. Instanciar o Crawler
    crawler = CnpqCrawler()
    
    try:
        # 3. Extrair os dados
        print(f"Extraindo dados de: {url}")
        data = crawler.get_data(url)
        
        # 4. Exibir algumas informações extraídas
        print("-" * 40)
        print(f"Nome do Grupo: {data.get('nome_grupo')}")
        print(f"Líderes: {data.get('lideres_do_grupo', [])}")
        
        if 'linhas_de_pesquisa' in data:
            print(f"Total de Linhas de Pesquisa: {len(data['linhas_de_pesquisa'])}")
            
        print("-" * 40)

        # 5. Exemplo de como salvar em JSON (Responsabilidade do Cliente)
        output_file = "demo_resultado.json"
        import json
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"Demonstração concluída! Dados salvos em: {output_file}")
        
    except Exception as e:
        print(f"Erro na demonstração: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
