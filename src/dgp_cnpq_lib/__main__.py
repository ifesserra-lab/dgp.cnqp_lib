import argparse
import json
import logging
import re
import sys

from .core import CnpqCrawler

# Initialize logger
logger = logging.getLogger(__name__)


def configure_logger(json_mode=False, verbose=False):
    """
    Configures the logger based on command-line arguments.
    """
    if verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    # Clear existing handlers to avoid duplicate output if called multiple times
    if logger.hasHandlers():
        logger.handlers.clear()

    handler = logging.StreamHandler(sys.stdout)
    if json_mode:
        # A more sophisticated JSON formatter would be needed here
        # For simplicity, we'll just output basic JSON for now or a placeholder
        formatter = logging.Formatter(
            '{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}'
        )
    else:
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def main():
    parser = argparse.ArgumentParser(
        description="Extract data from a CNPq research group mirror URL."
    )
    parser.add_argument("url", help="URL of the research group mirror")
    parser.add_argument("--output", "-o", help="Custom output JSON file path")
    parser.add_argument("--json-logs", action="store_true", help="Output logs in JSON format")
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose (DEBUG) logging"
    )

    args = parser.parse_args()

    configure_logger(json_mode=args.json_logs, verbose=args.verbose)

    crawler = CnpqCrawler()

    try:
        data = crawler.get_data(args.url)

        if args.output:
            filename = args.output
        else:
            # Sanitize filename
            group_name = data.get("nome_grupo", "grupo_pesquisa")
            safe_name = re.sub(r"[^\w\s-]", "", group_name).strip().lower()
            safe_name = re.sub(r"\s+", "_", safe_name)
            filename = f"{safe_name}.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        logger.info(f"Dados extraídos com sucesso e salvos em {filename}")

    except Exception as e:
        print(f"Erro ao extrair dados: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
