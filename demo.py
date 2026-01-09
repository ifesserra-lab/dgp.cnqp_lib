import sys
from dgp_cnpq_lib.core import CnpqCrawler
from dgp_cnpq_lib.logger import configure_logger, logger

def main():
    # 1. Configurar o Logger (Opcional - mas recomendado)
    configure_logger(verbose=True)
    
    logger.info("Iniciando demonstração do dgp_cnpq_lib...")

    # URL de exemplo (Espelho de Grupo)
    # Substitua por uma URL válida se necessário
    url = "http://dgp.cnpq.br/dgp/espelhogrupo/0225175815967657" 
    
    # 2. Instanciar o Crawler
    crawler = CnpqCrawler()
    
    try:
        # 3. Extrair os dados
        logger.info(f"Extraindo dados de: {url}")
        data = crawler.get_data(url)
        
        # 4. Exibir algumas informações extraídas
        print("-" * 40)
        print(f"Nome do Grupo: {data.get('nome_grupo')}")
        print(f"Líderes: {data.get('lideres_do_grupo', [])}")
        
        if 'linhas_de_pesquisa' in data:
            print(f"Total de Linhas de Pesquisa: {len(data['linhas_de_pesquisa'])}")
            
        print("-" * 40)
        logger.success("Demonstração concluída com sucesso!")
        
    except Exception as e:
        logger.error(f"Erro na demonstração: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
