print(">>> ECONOMY FILE LOADED <<<")

import random
import requests
from datetime import date
from discord.ext import commands

from database import (
    create_user,
    get_balance,
    get_last_daily,
    update_daily,
    trade_berries,
    get_shop_items,
    get_item,
    remove_berries,
    add_to_inventory,
    get_inventory,
    get_top_users
)   


class Economy(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # -----------------------------
    # Check Balance
    # -----------------------------
    @commands.command()
    async def bounty(self, ctx):
        create_user(ctx.author.id)

        balance = get_balance(ctx.author.id)

        await ctx.send(
            f"🏴‍☠️ {ctx.author.mention}\n"
            f"Your current bounty is **{balance} Berries**"
        )

    # -----------------------------
    # Daily Reward
    # -----------------------------
    @commands.command()
    async def setsail(self, ctx):
        create_user(ctx.author.id)

        last_daily = get_last_daily(ctx.author.id)
        today = str(date.today())

        if last_daily == today:
            await ctx.send(
                "⛵ You have already raided a merchant ship today!\n"
                "Come back tomorrow."
            )
            return

        reward = 200

        update_daily(ctx.author.id, reward)

        balance = get_balance(ctx.author.id)

        await ctx.send(
            f"🏴‍☠️ {ctx.author.mention}\n"
            f"You earned **{reward} Berries!**\n"
            f"Current Balance: **{balance} Berries**"
        )

    # -----------------------------
    # Trade Berries
    # -----------------------------
    @commands.command()
    async def trade(self, ctx, member: commands.MemberConverter, amount: int):

        create_user(ctx.author.id)
        create_user(member.id)

        if member == ctx.author:
            await ctx.send("❌ You can't trade with yourself!")
            return

        if amount <= 0:
            await ctx.send("❌ Enter a valid amount!")
            return

        balance = get_balance(ctx.author.id)

        if balance < amount:
            await ctx.send("❌ You don't have enough Berries!")
            return

        trade_berries(ctx.author.id, member.id, amount)

        await ctx.send(
            f"💰 {ctx.author.mention} traded **{amount} Berries** to {member.mention}!"
        )

    # -----------------------------
    # Shop
    # -----------------------------
    @commands.command()
    async def shop(self, ctx):

        items = get_shop_items()

        message = "🏴‍☠️ **Berry Broker Shop** 🏴‍☠️\n\n"

        for name, price, effect in items:
            message += (
                f"**{name}**\n"
                f"💰 Price: **{price} Berries**\n"
                f"✨ {effect}\n\n"
            )

        await ctx.send(message)

    # -----------------------------
    # Buy Item
    # -----------------------------
    @commands.command()
    async def buy(self, ctx, *, item_name):

        create_user(ctx.author.id)

        item = get_item(item_name)

        if item is None:
            await ctx.send("❌ That item doesn't exist!")
            return

        item_id, name, price, effect = item

        balance = get_balance(ctx.author.id)

        if balance < price:
            await ctx.send("❌ You don't have enough Berries!")
            return

        remove_berries(ctx.author.id, price)
        add_to_inventory(ctx.author.id, item_id)

        balance = get_balance(ctx.author.id)

        await ctx.send(
            f"🛒 {ctx.author.mention} bought **{name}** for **{price} Berries!**\n"
            f"💰 Remaining Balance: **{balance} Berries**"
        )

    # -----------------------------
    # Inventory
    # -----------------------------
    @commands.command()
    async def inventory(self, ctx):

        create_user(ctx.author.id)

        inventory = get_inventory(ctx.author.id)

        if not inventory:
            await ctx.send("📦 Your inventory is empty!")
            return

        message = f"🎒 **{ctx.author.display_name}'s Inventory**\n\n"

        for name, quantity in inventory:
            message += f"• **{name}** × {quantity}\n"

        await ctx.send(message)

    # -----------------------------
    # Worst Generation
    # -----------------------------
    @commands.command()
    async def worstgeneration(self, ctx):

        top_users = get_top_users()

        if not top_users:
            await ctx.send("No pirates have set sail yet!")
            return

        medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]

        message = "🏴‍☠️ **Worst Generation** 🏴‍☠️\n\n"

        for i, (user_id, berries) in enumerate(top_users):

            user = self.bot.get_user(user_id)

            if user is None:
                try:
                    user = await self.bot.fetch_user(user_id)
                    username = user.name
                except Exception:
                    username = f"Unknown ({user_id})"
            else:
                username = user.name

            message += (
                f"{medals[i]} **{username}** — 💰 {berries} Berries\n"
            )

        await ctx.send(message)

    # -----------------------------
    # Log Pose
    # -----------------------------
    @commands.command()
    async def logpose(self, ctx):

        endpoints = [
            "https://www.onepieceapi.com/api/characters",
            "https://www.onepieceapi.com/api/devil-fruits",
            "https://www.onepieceapi.com/api/bounties"
        ]

        url = random.choice(endpoints)

        try:
            response = requests.get(url)

            if response.status_code != 200:
                await ctx.send("❌ Failed to contact the One Piece API.")
                return

            data = response.json()

            if isinstance(data, dict):
                if "data" in data:
                    data = data["data"]
                elif "results" in data:
                    data = data["results"]

            if not data:
                await ctx.send("❌ No data found.")
                return

            item = random.choice(data)

            if "characters" in url:

                name = item.get("name", "Unknown")
                bounty = item.get("bounty", "Unknown")
                crew = item.get("crew", "Unknown")

                await ctx.send(
                    f"🧭 **Log Pose found a Pirate!**\n\n"
                    f"👤 **{name}**\n"
                    f"🏴 Crew: **{crew}**\n"
                    f"💰 Bounty: **{bounty}**"
                )

            elif "devil-fruits" in url:

                name = item.get("name", "Unknown")
                fruit_type = item.get("type", "Unknown")
                description = item.get(
                    "description",
                    "No description available."
                )

                await ctx.send(
                    f"🍈 **Devil Fruit Discovered!**\n\n"
                    f"**Name:** {name}\n"
                    f"**Type:** {fruit_type}\n\n"
                    f"{description}"
                )

            else:

                pirate = (
                    item.get("character")
                    or item.get("name")
                    or "Unknown"
                )

                amount = (
                    item.get("amount")
                    or item.get("bounty")
                    or "Unknown"
                )

                await ctx.send(
                    f"💰 **Wanted Poster Found!**\n\n"
                    f"👤 {pirate}\n"
                    f"🏴‍☠️ Bounty: **{amount}**"
                )

        except Exception as e:
            await ctx.send(f"❌ API Error:\n```{e}```")

    # -----------------------------
    # Raid
    # -----------------------------
    @commands.command()
    async def raid(self, ctx, member: commands.MemberConverter):

        create_user(ctx.author.id)
        create_user(member.id)

        if member == ctx.author:
            await ctx.send("❌ You can't raid yourself!")
            return

        attacker_balance = get_balance(ctx.author.id)
        defender_balance = get_balance(member.id)

        if defender_balance <= 0:
            await ctx.send("❌ That pirate has no Berries to steal!")
            return

        success = random.randint(1, 100)

        if success <= 70:

            stolen = random.randint(1, min(200, defender_balance))

            trade_berries(member.id, ctx.author.id, stolen)

            await ctx.send(
                f"🏴‍☠️ {ctx.author.mention} successfully raided {member.mention}!\n"
                f"💰 You stole **{stolen} Berries!**"
)

        else:

            fine = min(100, attacker_balance)

            if fine > 0:
                remove_berries(ctx.author.id, fine)

            await ctx.send(
                f"🚨 Marines caught {ctx.author.mention}!\n"
                f"💸 You paid **{fine} Berries** as a fine!"
            )


async def setup(bot):
    await bot.add_cog(Economy(bot))