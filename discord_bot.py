import discord
from discord.ext import commands
import os
from utils import get_gold_prices

# Setup Intents (Permissions)
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Discord Bot logged in as {bot.user}')

@bot.command()
async def gold(ctx):
    data = get_gold_prices()
    
    embed = discord.Embed(title="🌟 Bảng Giá Vàng (Gold Price)", color=0xFFD700)
    embed.add_field(name="🌍 Thế giới (World)", value=f"${data['world_price']} USD/oz", inline=False)
    embed.add_field(name="🇻🇳 SJC Mua (Buy)", value=f"{data['sjc_buy']} VND", inline=True)
    embed.add_field(name="🇻🇳 SJC Bán (Sell)", value=f"{data['sjc_sell']} VND", inline=True)
    embed.set_footer(text="Nguồn: tygia.com")
    
    await ctx.send(embed=embed)

async def start_discord_bot():
    token = os.getenv('discord_token')
    if not token:
        print("⚠️  Discord token missing!")
        return
    async with bot:
        await bot.start(token)
