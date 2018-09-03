import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from discord.utils import get

Client = discord.Client()
bot = commands.Bot(command_prefix = "p^")

token = "NDg1MDgzNzk4ODg3ODU4MTk3.DmranA.BSYVsfZZYHmqe5BYd_BHTlkxzSM"

@bot.event
async def on_ready():
    print("Parody Bot v.1.2.1")

@bot.command(pass_context=True)
@commands.has_role("AFC Manager")
async def ping(ctx):
    await bot.say("pong :ping_pong:")

@bot.command(pass_context=True)
@commands.has_role("AFC Manager")
async def check(ctx, user: discord.Member):
    embed = discord.Embed(title="Scanned {}...".format(user.name), description="Here's what I got", color=0xFFB6C1)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Creation Date", value=user.created_at, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("AFC Manager")
async def blacklist(ctx, name, reason):
    await bot.say("Added " + name + " to blacklist")
    await bot.send_message(bot.get_channel('484085835365482498'), "**" + name + "** " + reason)

@bot.command(pass_context=True)
@commands.has_role("AFC Manager")
async def clear(ctx, amount):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await bot.delete_messages(messages)
    await bot.send_message(bot.get_channel('483024209430446137'), "Messages deleted.")





bot.run(token)
