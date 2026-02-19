import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name="trading_bot", log_file="trading_bot.log"):
    """Set up and return a logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent double logging
    if logger.handlers:
        return logger

    # Create formatters
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File Handler
    file_handler = RotatingFileHandler(
        log_file, maxBytes=5*1024*1024, backupCount=2
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
