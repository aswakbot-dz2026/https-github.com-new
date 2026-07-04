import os
from dotenv import load_dotenv
load_dotenv()
MASTER_BOT_TOKEN = os.getenv("MASTER_BOT_TOKEN")
WORKER_1_TOKEN = os.getenv("WORKER_1_TOKEN")
WORKER_2_TOKEN = os.getenv("WORKER_2_TOKEN")
WORKER_3_TOKEN = os.getenv("WORKER_3_TOKEN")
EXCHANGE_NAME = os.getenv("EXCHANGE_NAME", "binance")
SYMBOL = os.getenv("SYMBOL", "BTC/USDT")
TIMEFRAME = os.getenv("TIMEFRAME", "1h")
CANDLE_LIMIT = int(os.getenv("CANDLE_LIMIT", "100"))
ANALYZER_STRATEGIES = {
    "bot1": {"name": "Trend", "indicators": ["EMA", "MACD"]},
    "bot2": {"name": "Momentum", "indicators": ["RSI", "STOCH"]},
    "bot3": {"name": "Volume", "indicators": ["BBANDS", "VOLUME"]}
}
