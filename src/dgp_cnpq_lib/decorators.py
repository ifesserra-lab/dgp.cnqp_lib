from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from playwright.sync_api import Error as PlaywrightError

def retry_handler():
    """
    Standard retry decorator for network operations.
    Policy:
    - Stop after 3 attempts.
    - Wait exponentially: 1s, 2s, 4s...
    - Retry on: PlaywrightError, TimeoutError, ConnectionError.
    """
    return retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        retry=retry_if_exception_type((PlaywrightError, TimeoutError, ConnectionError)),
        reraise=True
    )
