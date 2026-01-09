import time

from playwright.sync_api import sync_playwright

from .decorators import retry_handler
from .extractors import FieldsetParser
from .logger import logger


class CnpqCrawler:
    def __init__(self):
        self.parser = FieldsetParser()

    @retry_handler()
    def get_data(self, url: str) -> dict:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            logger.info(f"Navigating to {url}...")
            page.goto(url)

            # Wait for content to load
            page.wait_for_selector("fieldset", timeout=10000)

            # Just in case, scroll down
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1)

            result = {}

            # Extract Group Name
            try:
                h1 = page.query_selector("h1")
                if h1:
                    result["nome_grupo"] = h1.inner_text().strip()
                else:
                    result["nome_grupo"] = "grupo_sem_nome"
            except Exception:
                result["nome_grupo"] = "grupo_sem_nome"

            fieldsets = page.query_selector_all("fieldset")
            for fs in fieldsets:
                legend, content = self.parser.parse(fs)
                if legend:
                    key = self.parser.normalize_key(legend)
                    # Clean up empty sub-structures
                    if "outros_dados" in content and not content["outros_dados"]:
                        del content["outros_dados"]

                    result[key] = content

            browser.close()
            return result
