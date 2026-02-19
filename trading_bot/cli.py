import argparse

def parse_args():
    """Parse CLI arguments for the trading bot."""
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet CLI Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        type=str,
        required=True,
        help="Trading pair symbol (e.g., BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        type=str,
        required=True,
        choices=["BUY", "SELL"],
        help="Order side: BUY or SELL"
    )

    parser.add_argument(
        "--type",
        dest="order_type",
        type=str,
        required=True,
        choices=["MARKET", "LIMIT"],
        help="Order type: MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        type=float,
        required=True,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Limit price (required for LIMIT orders)"
    )

    args = parser.parse_args()

    # Post-parsing validation
    if args.order_type == "LIMIT" and args.price is None:
        parser.error("--price is required when --type is LIMIT")

    return args
