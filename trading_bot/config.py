import os
from dotenv import load_dotenv

# Load .env file if it exists
load_dotenv()

class Config:
    BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
    BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")
    # Use Testnet by default if BINANCE_USE_TESTNET is not set or set to True
    USE_TESTNET = os.getenv("BINANCE_USE_TESTNET", "True").lower() in ("true", "1", "t")
    
    # Futures Testnet Base URL
    FUTURES_TESTNET_URL = "https://testnet.binancefuture.com"

    @classmethod
    def validate(cls):
        """Validate that essential configurations are present."""
        missing = []
        if not cls.BINANCE_API_KEY:
            missing.append("BINANCE_API_KEY")
        if not cls.BINANCE_API_SECRET:
            missing.append("BINANCE_API_SECRET")
        
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
