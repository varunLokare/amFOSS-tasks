import asyncio

import discord
from discord.ext import commands

from database import create_shop_tables, add_shop_items
from config import TOKEN

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


async def load_extensions():
    print("Loading Economy Cog...")

    await bot.load_extension("cogs.economy")

    print("Economy Cog Loaded!")


async def main():

    # Create database tables
    create_shop_tables()

    # Insert default shop items
    add_shop_items()

    async with bot:
        await load_extensions()
        await bot.start(TOKEN)


asyncio.run(main())