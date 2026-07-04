import os
from dotenv import load_dotenv

load_dotenv()

MASTER_BOT_TOKEN = os.getenv("MASTER_BOT_TOKEN")
WORKER_1_TOKEN = os.getenv("WORKER_1_TOKEN")
WORKER_2_TOKEN = os.getenv("WORKER_2_TOKEN")
WORKER_3_TOKEN = os.getenv("WORKER_3_TOKEN")

EXCHANGE_NAME = os.getenv("EXCHANGE_NAME", "pionex")
DEFAULT_SYMBOL = os.getenv("SYMBOL", "BTC/USDT")

TIMEFRAMES = {
    "5m": "5 دقائق",
    "15m": "15 دقيقة", 
    "1h": "1 ساعة",
    "4h": "4 ساعات"
}

ASSETS = {
    "BTC": "BTC/USDT",
    "ETH": "ETH/USDT",
    "XAU": "XAU/USDT",
    "TSLAX": "TSLAX/USDT",
    "AAPLX": "AAPLX/USDT",
    "BRENT": "BRENTOIL/USDT",
    "WTI": "WTI/USDT",
    "XAG": "XAG/USDT",
    "NATGAS": "NATGAS/USDT"
}

ANALYZER_STRATEGIES = {
    "bot1": {"name": "Trend Following", "indicators": ["EMA", "MACD"]},
    "bot2": {"name": "Momentum", "indicators": ["RSI", "STOCH"]},
    "bot3": {"name": "Volatility", "indicators": ["BBANDS", "ATR"]}
}
