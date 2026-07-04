import os
import asyncio
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler
from config import MASTER_BOT_TOKEN, ASSETS, TIMEFRAMES
from analyzer_bot_1 import analyze as analyze1
from analyzer_bot_2 import analyze as analyze2
from analyzer_bot_3 import analyze as analyze3

SELECT_ASSET, SELECT_TIMEFRAME = range(2)

ASSET_KEYBOARD = ReplyKeyboardMarkup(
    [["BTC", "ETH", "XAU"], ["TSLAX", "AAPLX", "BRENT"], ["WTI", "XAG", "NATGAS"]],
    resize_keyboard=True
)

TIMEFRAME_KEYBOARD = ReplyKeyboardMarkup(
    [["5m", "15m"], ["1h", "4h"]],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 أهلاً بك في بوت تحليل Pionex!\n\nاختر الأصل:",
        reply_markup=ASSET_KEYBOARD
    )
    return SELECT_ASSET

async def select_asset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    asset = update.message.text.upper()
    if asset not in ASSETS:
        await update.message.reply_text("❌ الأصل غير مدعوم. اختر من القائمة.")
        return SELECT_ASSET
    
    context.user_data['asset'] = asset
    await update.message.reply_text(
        f"✅ اخترت: {asset}\n\nالآن اختر الفريم الزمني:",
        reply_markup=TIMEFRAME_KEYBOARD
    )
    return SELECT_TIMEFRAME

async def select_timeframe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    timeframe = update.message.text
    if timeframe not in TIMEFRAMES:
        await update.message.reply_text("❌ الفريم غير صحيح. اختر من القائمة.")
        return SELECT_TIMEFRAME
    
    asset = context.user_data['asset']
    symbol = ASSETS[asset]
    
    await update.message.reply_text(
        f"⏳ جاري تحليل {asset} على فريم {TIMEFRAMES[timeframe]}...",
        reply_markup=ReplyKeyboardRemove()
    )
    
    try:
        results = await asyncio.gather(
            analyze1(symbol, timeframe),
            analyze2(symbol, timeframe),
            analyze3(symbol, timeframe)
        )
        
        buy_votes = sum(1 for r in results if r[0] == "BUY")
        sell_votes = sum(1 for r in results if r[0] == "SELL")
        
        if buy_votes >= 2:
            signal = "🟢 شراء قوي"
        elif sell_votes >= 2:
            signal = "🔴 بيع قوي"
        else:
            signal = "⚪ انتظار/محايد"
        
        details = "\n".join([f"• {r[2]}" for r in results])
        
        await update.message.reply_text(
            f"📊 **نتيجة التحليل**\n\n"
            f"💰 الأصل: {asset}\n"
            f"⏰ الفريم: {TIMEFRAMES[timeframe]}\n"
            f"📈 الإشارة: {signal}\n\n"
            f"📝 التفاصيل:\n{details}\n\n"
            f"لتحليل جديد اضغط /start",
            parse_mode='Markdown'
        )
        
    except Exception as e:
        await update.message.reply_text(f"❌ خطأ: {str(e)}")
    
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تم الإلغاء.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

def main():
    application = Application.builder().token(MASTER_BOT_TOKEN).build()
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            SELECT_ASSET: [MessageHandler(filters.TEXT & ~filters.COMMAND, select_asset)],
            SELECT_TIMEFRAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, select_timeframe)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )
    
    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == "__main__":
    main()
