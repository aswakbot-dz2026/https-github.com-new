import os
from utils import fetch_ohlcv
from telegram.ext import Application, CommandHandler
from config import ANALYZER_STRATEGIES
TOKEN = os.getenv("WORKER_3_TOKEN")
async def analyze(symbol):
    df = fetch_ohlcv(symbol, '1h', 100)
    last = df.iloc[-1]
    if last['volume'] > df['volume'].mean():
        return "BUY", 0.7, "حجم مرتفع"
    return "HOLD", 0.5, "حجم عادي"
def main():
    app = Application.builder().token(TOKEN).build()
    app.run_polling()
if __name__ == "__main__":
    main()
