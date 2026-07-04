import ccxt
import pandas as pd
import pandas_ta as ta

exchange = getattr(ccxt, 'pionex')()

def fetch_ohlcv(symbol: str, timeframe: str, limit: int = 100):
    try:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df
    except Exception as e:
        print(f"Error: {e}")
        raise
