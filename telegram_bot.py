import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from utils import get_gold_prices

async def view_gold(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_gold_prices()
    
    msg = (
        f"🌟 **CẬP NHẬT GIÁ VÀNG** 🌟\n\n"
        f"🌍 **World:** ${data['world_price']} USD/oz\n"
        f"-----------------\n"
        f"🇻🇳 **SJC Mua:** {data['sjc_buy']} VND\n"
        f"🇻🇳 **SJC Bán:** {data['sjc_sell']} VND\n"
    )
    await update.message.reply_text(msg, parse_mode='Markdown')

async def start_telegram_bot():
    token = os.getenv('telegram_token')
    if not token:
        print("⚠️  Telegram token missing!")
        return

    application = ApplicationBuilder().token(token).build()
    application.add_handler(CommandHandler("gold", view_gold))

    await application.initialize()
    await application.start()
    print("✅ Telegram Bot is ready")
    await application.updater.start_polling()
