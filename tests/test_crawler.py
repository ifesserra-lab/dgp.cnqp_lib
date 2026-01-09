from unittest.mock import MagicMock, patch

from dgp_cnpq_lib.core import CnpqCrawler


def test_crawler_initialization():
    crawler = CnpqCrawler()
    assert crawler.parser is not None


@patch("dgp_cnpq_lib.core.sync_playwright")
def test_get_data_mocked(mock_playwright):
    # Setup Mock
    mock_browser = MagicMock()
    mock_page = MagicMock()
    mock_context = MagicMock()

    mock_playwright.return_value.__enter__.return_value = mock_context
    mock_context.chromium.launch.return_value = mock_browser
    mock_browser.new_page.return_value = mock_page

    # Mock H1 for group name
    mock_h1 = MagicMock()
    mock_h1.inner_text.return_value = "Grupo Mock"

    # Configure page logic
    def query_selector_side_effect(selector):
        if selector == "h1":
            return mock_h1
        return None

    mock_page.query_selector.side_effect = query_selector_side_effect
    mock_page.query_selector_all.return_value = []  # No fieldsets for this simple test

    # Execute
    crawler = CnpqCrawler()
    result = crawler.get_data("http://fake.url")

    # Assert
    assert result["nome_grupo"] == "Grupo Mock"
    mock_page.goto.assert_called_with("http://fake.url")
