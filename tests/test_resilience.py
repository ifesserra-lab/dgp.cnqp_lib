from unittest.mock import MagicMock, patch
import pytest
from playwright.sync_api import Error as PlaywrightError
from dgp_cnpq_lib.core import CnpqCrawler

def test_retry_on_timeout():
    """Verify that get_data retries 3 times on PlaywrightError."""
    
    # Mock sync_playwright to simulate failures
    with patch("dgp_cnpq_lib.core.sync_playwright") as mock_playwright:
        mock_p = MagicMock()
        mock_playwright.return_value.__enter__.return_value = mock_p
        
        # Configure launch to raise PlaywrightError
        mock_p.chromium.launch.side_effect = PlaywrightError("Timeout occurred")
        
        crawler = CnpqCrawler()
        
        # Expect the exception after retries
        with pytest.raises(PlaywrightError):
            crawler.get_data("http://example.com")
            
        # Verify launch was called 3 times (initial + 2 retries or 3 total attempts)
        assert mock_p.chromium.launch.call_count == 3
