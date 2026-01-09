import json
import re
import sys

from .core import CnpqCrawler


def main():
    if len(sys.argv) < 2:
        print("Uso: python -m dgp_cnpq_lib <url>")
        sys.exit(1)

    url = sys.argv[1]
    crawler = CnpqCrawler()

    try:
        data = crawler.get_data(url)

        # Sanitize filename
        group_name = data.get("nome_grupo", "grupo_pesquisa")
        safe_name = re.sub(r"[^\w\s-]", "", group_name).strip().lower()
        safe_name = re.sub(r"\s+", "_", safe_name)

        filename = f"{safe_name}.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"Dados extraídos com sucesso e salvos em {filename}")

    except Exception as e:
        print(f"Erro ao extrair dados: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
