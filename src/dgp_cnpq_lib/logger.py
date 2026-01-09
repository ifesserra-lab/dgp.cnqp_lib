import sys
from loguru import logger

def configure_logger(json_mode: bool = False, verbose: bool = False):
    """
    Configures loguru logger.
    - json_mode: If True, logs in JSON format (good for pipelines).
    - verbose: If True, level is DEBUG, else INFO.
    """
    logger.remove()
    
    level = "DEBUG" if verbose else "INFO"
    
    if json_mode:
        logger.add(sys.stderr, format="{message}", serialize=True, level=level)
    else:
        logger.add(sys.stderr, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <level>{message}</level>", level=level)

# Clean default and start with basic config
logger.remove()
logger.add(sys.stderr, level="INFO")
