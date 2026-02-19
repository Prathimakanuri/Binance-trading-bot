# Binance Futures Testnet CLI Trading Bot

A production-ready Python CLI application for placing orders on the Binance Futures Testnet (USDT-M).

## Features

- **Order Types**: Supports `MARKET` and `LIMIT` orders.
- **Sides**: Supports `BUY` and `SELL`.
- **Logging**: Detailed logs of API activity in `trading_bot.log`.
- **Validation**: Strict CLI input validation and clear error reporting.

## Setup Steps

1. **Prerequisites**:
   - Python 3.10+
   - Binance Futures Testnet API Key and Secret. Register at [testnet.binancefuture.com](https://testnet.binancefuture.com/).

2. **Clone the repository** (if applicable) or navigate to the project directory.

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and replace the placeholders with your API credentials:
   ```text
   BINANCE_API_KEY=your_testnet_api_key
   BINANCE_API_SECRET=your_testnet_api_secret
   BINANCE_USE_TESTNET=True
   ```

## How to Run Examples

### 1. View Help
```bash
python main.py --help
```

### 2. Market Buy Order
Place a market buy order for 0.001 BTC:
```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### 3. Limit Sell Order
Place a limit sell order for 0.001 BTC at $100,000:
```bash
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 100000
```

## Assumptions & Notes

- **USDT-M Futures Only**: This bot is specifically designed for USDT-Margined futures on the Binance Testnet.
- **Asset Availability**: The bot assumes you have sufficient USDT margin in your Testnet account to cover the orders.
- **Symbol Format**: Symbols should be provided in the standard Binance format (e.g., `BTCUSDT`, `ETHUSDT`).
- **Precision**: Quantity and Price precision should match the specific requirements of the trading pair on Binance.
- **Network**: A stable internet connection is required for API communication.
- **Time In Force**: LIMIT orders default to `GTC` (Good Till Cancelled).

## Logging

All API requests, responses, and errors are logged to `trading_bot.log` located in the root directory. The log file is configured with rotation (max 5MB, 2 backups).
