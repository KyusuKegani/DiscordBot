import discord
import settings
import stage
import formatter
from discord.ext import commands

STATUS_ERROR_MESSAGE = "APIサーバエラーでし！！！！！"

BOT_TOKEN = settings.BT

# https://qiita.com/junpiiiiiiik/items/79c2219da6b5e2c06ed8
bot = commands.Bot(command_prefix="/")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def gachi(ctx):
    try:
        msgList = stage.getstage("gachi")
    except Exception:
        await ctx.send(STATUS_ERROR_MESSAGE)
    embed = discord.Embed(title="**これからのガチマッチ**", color=0xf71f71)
    embed = formatter.embedformat(embed, msgList)
    await ctx.send(embed=embed)


@bot.command()
async def reg(ctx):
    try:
        msgList = stage.getstage("regular")
    except Exception:
        await ctx.send(STATUS_ERROR_MESSAGE)
    embed = discord.Embed(title="**これからのレギュラーマッチ**", color=0xf71f71)
    embed = formatter.embedformat(embed, msgList)
    await ctx.send(embed=embed)


@bot.command()
async def leag(ctx):
    try:
        msgList = stage.getstage("league")
    except Exception:
        await ctx.send(STATUS_ERROR_MESSAGE)
    embed = discord.Embed(title="**これからのリーグマッチ**", color=0xf71f71)
    embed = formatter.embedformat(embed, msgList)
    await ctx.send(embed=embed)

bot.run(BOT_TOKEN)
