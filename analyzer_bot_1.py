import os
from utils import fetch_ohlcv
from telegram.ext import Application, CommandHandler
from config import ANALYZER_STRATEGIES
TOKEN = os.getenv("WORKER_1_TOKEN")
async def analyze(symbol):
    df = fetch_ohlcv(symbol, '1h', 100)
    last = df.iloc[-1]
    if last['close'] > last['open']:
        return "BUY", 0.8, "اتجاه صاعد"
    return "SELL", 0.8, "اتجاه هابط"
def main():
    app = Application.builder().token(TOKEN).build()
    app.run_polling()
if __name__ == "__main__":
    main()
