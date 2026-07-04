import os
from utils import fetch_ohlcv
from telegram.ext import Application, CommandHandler
from config import ANALYZER_STRATEGIES
import random
TOKEN = os.getenv("WORKER_2_TOKEN")
async def analyze(symbol):
    df = fetch_ohlcv(symbol, '1h', 100)
    signals = [("BUY", 0.75, "زخم شرائي"), ("SELL", 0.75, "زخم بيعي"), ("HOLD", 0.5, "محايد")]
    return random.choice(signals)
def main():
    app = Application.builder().token(TOKEN).build()
    app.run_polling()
if __name__ == "__main__":
    main()
