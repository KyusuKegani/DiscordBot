import discord
import settings
import gachi
import formatter

STATUS_ERROR_MESSAGE = "APIサーバエラーでし！！！！！"

BOT_TOKEN = settings.BT
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


# API
@client.event
async def on_message(message):
    if message.content in {'gachi', 'gati', 'ガチマ'}:
        # 送り主がBotだった場合反応しない
        if client.user != message.author:
            try:
                msgList = gachi.getstage()
            except Exception:
                await client.send_message(message.channel,
                                          STATUS_ERROR_MESSAGE)
                # 一度ベタ書きで実装、あとでリファクタリング
            embed = discord.Embed(title="**これからのガチマッチ**", colour=0xfdf5e4)
            embed = formatter.embedformat(embed, msgList)
            await client.send_message(message.channel, embed=embed)


client.run(BOT_TOKEN)
