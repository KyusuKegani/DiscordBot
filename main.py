#!/usr/bin/python
# -*- coding: utf-8 -*-

import discord
import settings
import stage
import formatter
from discord.ext import commands

STATUS_ERROR_MESSAGE = "エラーでし！！！！！"

BOT_TOKEN = settings.BT
REGULAR_COLOR = 0x95d10a
GACHI_COLOR = 0xf2660d
LEAGUE_COLOR = 0xf12e7d
SALMON_COLOR = 0xe35226

# スマホからの入力のしやすさを考慮して接頭辞"/"に、Discordのものとも被っているので変更する予定有り
bot = commands.Bot(command_prefix={"/"})


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


# ガチマッチのステージ情報を取得するコマンド
@bot.command()
async def gachi(ctx):
    try:
        msgList = stage.get_stage("gachi")
    except Exception:
        await ctx.send(STATUS_ERROR_MESSAGE)
    embed = discord.Embed(title="**これからのガチマッチでし！**", color=GACHI_COLOR)
    embed = formatter.stage_embed_format(embed, msgList)
    await ctx.send(embed=embed)


# レギュラーマッチのステージ情報を取得するコマンド
@bot.command()
async def reg(ctx):
    try:
        msgList = stage.get_stage("regular")
    except Exception:
        await ctx.send(STATUS_ERROR_MESSAGE)
    embed = discord.Embed(title="**これからのレギュラーマッチでし！**", color=REGULAR_COLOR)
    embed = formatter.stage_embed_format(embed, msgList)
    await ctx.send(embed=embed)


# regコマンドと同様、Botに柔軟性を持たせるため、別コマンドでも実装
@bot.command()
async def regular(ctx):
    try:
        msgList = stage.get_stage("regular")
    except Exception:
        await ctx.send(STATUS_ERROR_MESSAGE)
    embed = discord.Embed(title="**これからのレギュラーマッチでし！**", color=REGULAR_COLOR)
    embed = formatter.stage_embed_format(embed, msgList)
    await ctx.send(embed=embed)


# リーグマッチのステージ情報を取得するコマンド
@bot.command()
async def leag(ctx):
    try:
        msgList = stage.get_stage("league")
    except Exception:
        await ctx.send(STATUS_ERROR_MESSAGE)
    embed = discord.Embed(title="**これからのリーグマッチでし！**", color=LEAGUE_COLOR)
    embed = formatter.stage_embed_format(embed, msgList)
    await ctx.send(embed=embed)


# leagコマンドと同様、Botに柔軟性を持たせるために実装
@bot.command()
async def league(ctx):
    try:
        msgList = stage.get_stage("league")
    except Exception:
        await ctx.send(STATUS_ERROR_MESSAGE)
    embed = discord.Embed(title="**これからのリーグマッチでし！**", color=LEAGUE_COLOR)
    embed = formatter.stage_embed_format(embed, msgList)
    await ctx.send(embed=embed)


# サーモンランのステージ情報を取得するためのコマンド
@bot.command()
async def salmon(ctx):
    try:
        msgList = stage.get_salmon()
    except Exception:
        await ctx.send(STATUS_ERROR_MESSAGE)
    embed = discord.Embed(title="**これからのサーモンランでし！**", color=SALMON_COLOR)
    embed = formatter.salmon_embed_format(embed, msgList)
    await ctx.send(embed=embed)


# サーモンランのステージ情報を取得するためのコマンド(salmonと同一)
@bot.command()
async def shake(ctx):
    try:
        msgList = stage.get_salmon()
    except Exception:
        await ctx.send(STATUS_ERROR_MESSAGE)
    embed = discord.Embed(title="**これからのサーモンランでし！**", color=SALMON_COLOR)
    embed = formatter.salmon_embed_format(embed, msgList)
    await ctx.send(embed=embed)


# サーモンランのステージ情報を取得するためのコマンド(salmonと同一)
@bot.command()
async def sake(ctx):
    try:
        msgList = stage.get_salmon()
    except Exception:
        await ctx.send(STATUS_ERROR_MESSAGE)
    embed = discord.Embed(title="**これからのサーモンランでし！**", color=SALMON_COLOR)
    embed = formatter.salmon_embed_format(embed, msgList)
    await ctx.send(embed=embed)


@bot.command()
async def ran2(ctx):
    try:
        msgList = stage.get_salmon()
    except Exception:
        await ctx.send(STATUS_ERROR_MESSAGE)
    embed = discord.Embed(title="**ランダムにブキを割り当てたでし！**", color=SALMON_COLOR)
    embed = formatter.salmon_embed_format(embed, msgList)
    await ctx.send(embed=embed)


@bot.command()
async def random2(ctx):
    try:
        msgList = stage.get_salmon()
    except Exception:
        await ctx.send(STATUS_ERROR_MESSAGE)
    embed = discord.Embed(title="**ランダムにブキを割り当てたでし！**", color=SALMON_COLOR)
    embed = formatter.salmon_embed_format(embed, msgList)
    await ctx.send(embed=embed)


bot.remove_command("help")


# helpコマンドの実装、コマンドを追加した際にはここを編集すること！！！！！
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="ブキチBot(改)",
        description="Splatoon2の各種ステージ情報を教えてくれるBotでし。コマンドはイカの通りでし！！！！！",
        color=0xf71f71)
    embed.add_field(name="/gachi", value="現在+4回分のガチマッチのルール/ステージを表示します")
    embed.add_field(
        name="/reg or regular", value="現在+4回分のレギュラーステージを表示します、ついでにルールも")
    embed.add_field(
        name="/leag or league", value="現在+4回分のリーグマッチのルール/ステージを表示します")
    embed.add_field(
        name="/salmon or sake or shake", value="現在わかっているサーモンランのステージを表示します")
    embed.add_field(name="/help", value="このコマンドです、このBotのコマンド一覧を表示します")
    embed.add_field(name="/info", value="このBotの情報を表示します")
    await ctx.send(embed=embed)


# infoコマンド、Botに関するメタ的な情報を格納
@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="ブキチBot(改) ver 1.0.1",
        description="Splatoon2の各種ステージ情報を教えてくれるBotでし！！！！！！！",
        color=0xf71f71)
    embed.add_field(name="作成者", value="Yusuke Sabi")
    embed.add_field(
        name="ソースコード", value="https://github.com/YusukeSabi/DiscordBot")
    await ctx.send(embed=embed)


bot.run(BOT_TOKEN)
