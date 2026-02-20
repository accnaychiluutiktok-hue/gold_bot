import asyncio
import os
from dotenv import load_dotenv
from discord_bot import start_discord_bot
from telegram_bot import start_telegram_bot
from keep_alive import keep_alive 

# Load .env variables (only needed for local testing)
load_dotenv()

async def main():
    # 1. Start Web Server
    keep_alive()
    
    # 2. Start Bots concurrently
    print("🚀 Starting all systems...")
    await asyncio.gather(
        start_discord_bot(),
        start_telegram_bot()
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🛑 Stopped by user")
