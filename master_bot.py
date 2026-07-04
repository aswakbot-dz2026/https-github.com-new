import os
import asyncio
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from analyzer_bot_1 import analyze as analyze1
from analyzer_bot_2 import analyze as analyze2
from analyzer_bot_3 import analyze as analyze3
TOKEN = os.getenv("MASTER_BOT_TOKEN")
KEYBOARD = ReplyKeyboardMarkup([['BTC', 'ETH', 'BNB']], resize_keyboard=True)
async def start(update, context):
    await update.message.reply_text("أرسل العملة:", reply_markup=KEYBOARD)
async def handle_symbol(update, context):
    symbol = update.message.text.upper() + "/USDT"
    results = await asyncio.gather(analyze1(symbol), analyze2(symbol), analyze3(symbol))
    buy_votes = sum(1 for r in results if r[0] == "BUY")
    sell_votes = sum(1 for r in results if r[0] == "SELL")
    final = "🟢 شراء" if buy_votes >= 2 else "🔴 بيع" if sell_votes >= 2 else "⚪ انتظار"
    await update.message.reply_text(f"النتيجة: {final}")
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_symbol))
    app.run_polling()
if __name__ == "__main__":
    main()
