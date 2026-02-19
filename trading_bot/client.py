from binance.client import Client
from binance.exceptions import BinanceAPIException
import logging

class BinanceClient:
    def __init__(self, api_key: str, api_secret: str, testnet: bool = True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        self.logger = logging.getLogger("trading_bot.client")

    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
        """
        Place a futures order.
        :param symbol: e.g., 'BTCUSDT'
        :param side: 'BUY' or 'SELL'
        :param order_type: 'MARKET' or 'LIMIT'
        :param quantity: float
        :param price: required for LIMIT orders
        """
        try:
            params = {
                'symbol': symbol.upper(),
                'side': side.upper(),
                'type': order_type.upper(),
                'quantity': quantity,
            }

            if order_type.upper() == 'LIMIT':
                if price is None:
                    raise ValueError("Price is required for LIMIT orders.")
                params['price'] = str(price)
                params['timeInForce'] = 'GTC'  # Good Till Cancelled

            self.logger.info(f"Sending order request: {params}")
            
            # Use futures_create_order for USDT-M Futures
            response = self.client.futures_create_order(**params)
            
            self.logger.info(f"Order response received: {response}")
            return response

        except BinanceAPIException as e:
            self.logger.error(f"Binance API Error: {e.status_code} - {e.message}")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error placing order: {str(e)}")
            raise
