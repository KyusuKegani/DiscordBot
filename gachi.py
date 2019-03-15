import requests
import json
import formatter
import discord

STATUS_OK = 200
DATE_FORMAT = '%Y-%m-%dT%H:%M:%S'
MESSAGE_FORMAT_SAME_DAY = """** {0}/{1} {2}時 - {3}時 **"""
MESSAGE_FORMAT_DIFFERENT_DAY = """** {0}/{1} {2}時 - {3}/{4} {5}時 **"""
MESSAGE_FORMAT_RULE = """      **ルール:** {0}"""
MESSAGE_FORMAT_STAGE = """      **ステージ:** {0},{1}"""


def getstage():
    # 非公式API: https://spla2.yuu26.com/
    url_now = 'https://spla2.yuu26.com/gachi/now'
    url_next = 'https://spla2.yuu26.com/gachi/next_all'
    # APIの利用方法によりUser Agentを偽装
    ua = 'Discord Bot/0.1 (twitter @bser_assistant)'
    headers = {'User-Agent': ua}
    res_now = requests.get(url_now, headers=headers)
    res_next = requests.get(url_next, headers=headers)
    msgList = []
    if (res_next.status_code == STATUS_OK
            and res_now.status_code == STATUS_OK):
        # STATUSが200であることを確認してからパースする
        lists_now = json.loads(res_now.text)
        lists_next = json.loads(res_next.text)

        # embed形式にフォーマットを行う
        discord.Embed(title="ガチマッチのスケジュール", colour=0x3498db)

        # stageformatを用いて現在のステージから1つを取得、embedに情報を埋め込み
        msgList.extend(formatter.stageformat(lists_now["result"], 1))
        # stageformatを用いてこれからのステージから4つ分を取得、embedに情報を埋め込み
        msgList.extend(formatter.stageformat(lists_next["result"], 4))

        # TODO:今のステージの画像を二つくっつける
        # embed.set_thumbnail(url="https://app.splatoon2.nintendo.net/images/stage/132327c819abf2bd44d0adc0f4a21aad9cc84bb2.png")

        return msgList
    else:
        raise Exception("BAD STATUS")
