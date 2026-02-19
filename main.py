import sys
import json
from trading_bot.config import Config
from trading_bot.logger import setup_logger
from trading_bot.client import BinanceClient
from trading_bot.cli import parse_args
from binance.exceptions import BinanceAPIException

def main():
    # Parse arguments first so --help works without config
    args = parse_args()

    # Initialize logger
    logger = setup_logger()
    
    try:
        # Load and validate config
        Config.validate()
    except ValueError as e:
        logger.error(f"Configuration Error: {e}")
        print(f"ERROR: {e}")
        print("Please ensure you have a .env file with BINANCE_API_KEY and BINANCE_API_SECRET.")
        sys.exit(1)

    # Initialize Binance client
    try:
        bot_client = BinanceClient(
            api_key=Config.BINANCE_API_KEY,
            api_secret=Config.BINANCE_API_SECRET,
            testnet=Config.USE_TESTNET
        )
    except Exception as e:
        logger.error(f"Failed to initialize Binance Client: {e}")
        print(f"ERROR: Failed to initialize Binance Client: {e}")
        sys.exit(1)

    # Log order request summary
    order_summary = {
        "symbol": args.symbol,
        "side": args.side,
        "type": args.order_type,
        "quantity": args.quantity,
        "price": args.price
    }
    logger.info(f"Placing order: {order_summary}")
    print("\n--- Order Request Summary ---")
    for k, v in order_summary.items():
        if v is not None:
            print(f"{k.capitalize()}: {v}")
    print("-----------------------------\n")

    # Place order
    try:
        response = bot_client.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.order_type,
            quantity=args.quantity,
            price=args.price
        )
        
        # Print success and response details
        print("SUCCESS: Order placed successfully!")
        print("\n--- Order Response Details ---")
        # Extract requested fields
        print(f"OrderId: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")
        print("------------------------------\n")
        
        logger.info(f"Order successfully placed. OrderId: {response.get('orderId')}")

    except BinanceAPIException as e:
        # Already logged in client.py
        print(f"API ERROR: {e.message}")
        sys.exit(1)
    except Exception as e:
        # Already logged in client.py
        print(f"UNEXPECTED ERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
