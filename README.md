Here is a professional, ready-to-use `README.md` for your new Gold Bot repository. It includes all the features we discussed, setup instructions, and the Render deployment guide.

Copy the text inside the box below and paste it into your `README.md` file on GitHub:

```markdown
# 🌟 Gold Price Bot (Discord & Telegram)

A Python-based bot that tracks and reports live gold prices (Vietnamese SJC & World). The bot runs concurrently on both Discord and Telegram, and is optimized for free 24/7 cloud hosting.

## ✨ Features
- **Multi-Platform:** Runs on both Discord and Telegram simultaneously using `asyncio`.
- **Live Data:** Fetches real-time SJC Gold and World Gold prices.
- **Commands:** 
  - Discord: Type `!gold`
  - Telegram: Type `/gold`
- **Cloud-Ready:** Includes a built-in Flask server (`keep_alive.py`) to keep the bot running 24/7 on free hosts like Render.com.

---

## 🛠️ Local Setup & Installation

Follow these steps to run the bot on your own computer.

### 1. Clone the repository
```bash
git clone https://github.com/accnaychiluutiktok-hue/gold_bot.git
cd gold_bot
```

### 2. Install Dependencies
Make sure you have Python 3.8+ installed. Run this command in your terminal:
```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables
**Never share your bot tokens!** 
Create a file named `.env` in the root folder of the project and add your tokens:

```env
discord_token=YOUR_DISCORD_BOT_TOKEN_HERE
telegram_token=YOUR_TELEGRAM_BOT_TOKEN_HERE
```
*(Note: Ensure `.env` is listed inside your `.gitignore` file so it doesn't get uploaded to GitHub).*

### 4. Run the Bot
```bash
python main.py
```
You should see messages indicating that the web server, Discord bot, and Telegram bot have all started successfully.

---

## ☁️ Deploying 24/7 to Render.com (Free)

This bot is configured to easily deploy on Render.

1. Create an account on [Render](https://render.com/).
2. Go to Dashboard -> **New +** -> **Web Service**.
3. Connect this GitHub repository.
4. Fill in the following deployment settings:
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python main.py`
   - **Instance Type:** `Free`
5. **Crucial Step:** Scroll down to **Environment Variables** and add your tokens:
   - Key: `discord_token` | Value: `your_discord_token`
   - Key: `telegram_token` | Value: `your_telegram_token`
6. Click **Create Web Service**.

### Keeping it awake
Free Render services go to sleep after 15 minutes of inactivity. To prevent this:
1. Copy the web URL Render gives you (e.g., `https://gold-bot-xyz.onrender.com`).
2. Go to [UptimeRobot](https://uptimerobot.com/) (free).
3. Create a new HTTP monitor pointing to your Render URL and set it to ping every 5 minutes.

---

## 📂 Project Structure
- `main.py`: The orchestrator that runs the bots and the web server.
- `discord_bot.py`: Handles Discord connection and embed formatting.
- `telegram_bot.py`: Handles Telegram commands and markdown formatting.
- `utils.py`: Contains the web-scraping/API logic to fetch gold prices.
- `keep_alive.py`: A lightweight Flask server for cloud deployment.
- `requirements.txt`: Python dependencies.

## 📝 Disclaimer
This bot fetches data from public financial websites. It is intended for educational and personal use. Always verify financial data through official channels.
```
