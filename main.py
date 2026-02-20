import os
import requests
import time
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
from utils import get_gold_prices
from keep_alive import keep_alive

# Load variables from .env (for local testing)
load_dotenv()

def send_discord_webhook(data):
    webhook_url = os.getenv('discord_webhook')
    if not webhook_url:
        print("⚠️ discord_webhook not found.")
        return

    # Format the message for Discord
    embed = {
        "title": "🌟 Bảng Giá Vàng (Gold Price)",
        "color": 16766720, # Gold color hex
        "fields": [
            {"name": "🌍 Thế giới (World)", "value": f"${data['world_price']} USD/oz", "inline": False},
            {"name": "🇻🇳 SJC Mua (Buy)", "value": f"{data['sjc_buy']} VND", "inline": True},
            {"name": "🇻🇳 SJC Bán (Sell)", "value": f"{data['sjc_sell']} VND", "inline": True}
        ],
        "footer": {"text": "Nguồn: tygia.com"}
    }
    
    # Send to Discord
    response = requests.post(webhook_url, json={"embeds": [embed]})
    if response.status_code == 204:
        print("✅ Sent alert to Discord!")
    else:
        print(f"❌ Failed to send to Discord: {response.status_code}")

def send_telegram_message(data):
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    
    if not token or not chat_id:
        print("⚠️ TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID not found.")
        return

    # Format the message for Telegram
    msg = (
        f"🌟 *CẬP NHẬT GIÁ VÀNG* 🌟\n\n"
        f"🌍 *World:* ${data['world_price']} USD/oz\n"
        f"-----------------\n"
        f"🇻🇳 *SJC Mua:* {data['sjc_buy']} VND\n"
        f"🇻🇳 *SJC Bán:* {data['sjc_sell']} VND\n"
    )
    
    # Send to Telegram
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": msg,
        "parse_mode": "Markdown"
    }
    
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ Sent alert to Telegram!")
    else:
        print(f"❌ Failed to send to Telegram: {response.text}")

def run_alerts():
    print("Fetching new gold prices...")
    data = get_gold_prices()
    send_discord_webhook(data)
    send_telegram_message(data)

if __name__ == "__main__":
    # 1. Start the web server to keep Render awake
    keep_alive()
    
    # 2. Run the alert once immediately when the bot starts
    run_alerts()

    # 3. Schedule the bot to run every X minutes
    # Currently set to 60 minutes. You can change this number!
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_alerts, 'interval', minutes=60)
    scheduler.start()
    
    print("🚀 Auto-Alert Scheduler started. Press Ctrl+C to exit.")
    
    # Keep the script running
    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
