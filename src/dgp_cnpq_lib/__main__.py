import argparse
import json
import re
import sys

from .core import CnpqCrawler
from .logger import configure_logger, logger


def main():
    parser = argparse.ArgumentParser(description="CNPq Research Group Extractor")
    parser.add_argument("url", help="URL of the research group mirror")
    parser.add_argument("--json-logs", action="store_true", help="Output logs in JSON format")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose (DEBUG) logging")

    args = parser.parse_args()

    configure_logger(json_mode=args.json_logs, verbose=args.verbose)

    crawler = CnpqCrawler()

    try:
        data = crawler.get_data(args.url)

        # Sanitize filename
        group_name = data.get("nome_grupo", "grupo_pesquisa")
        safe_name = re.sub(r"[^\w\s-]", "", group_name).strip().lower()
        safe_name = re.sub(r"\s+", "_", safe_name)

        filename = f"{safe_name}.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        logger.info(f"Dados extraídos com sucesso e salvos em {filename}")

    except Exception as e:
        logger.error(f"Erro ao extrair dados: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
