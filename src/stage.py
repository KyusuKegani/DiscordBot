import requests
import json
import formatter

STATUS_OK = 200
USER_AGENT = "Discord Bukichi Bot/v1.1 (twitter @bser_assistant)"


def get_salmon():
    # 非公式APIの　https://spla2.yuu26.com/ のURL
    url = 'https://spla2.yuu26.com/coop/schedule'

    # APIの利用方法に指定があるためUser Agentを偽装
    headers = {'User-Agent': USER_AGENT}

    res = requests.get(url, headers=headers)

    msgList = []

    if (res.status_code == STATUS_OK):
        lists = json.loads(res.text)
        # stageformatを用いて現在のステージから1つを取得
        msgList.extend(formatter.salmon_format(lists["result"]))
        return msgList
    else:
        raise Exception("BAD STATUS")


# APIを叩いてステージ情報を取得する。
# rule: 取得したいルール
def get_stage(rule):
    # 非公式API: https://spla2.yuu26.com/ のURLの生成
    url_now = 'https://spla2.yuu26.com/{0}/now'.format(rule)
    url_next = 'https://spla2.yuu26.com/{0}/next_all'.format(rule)

    # APIの利用方法に指定があるためUser Agentを偽装
    headers = {'User-Agent': USER_AGENT}

    res_now = requests.get(url_now, headers=headers)
    res_next = requests.get(url_next, headers=headers)
    msgList = []

    # STATUSが200であることを確認してからパースする
    if (res_next.status_code == STATUS_OK
            and res_now.status_code == STATUS_OK):

        lists_now = json.loads(res_now.text)
        lists_next = json.loads(res_next.text)

        # stageformatを用いて現在のステージから1つを取得
        msgList.extend(formatter.stage_format(lists_now["result"], 1))
        # stageformatを用いてこれからのステージから4つ分を取得
        msgList.extend(formatter.stage_format(lists_next["result"], 4))

        # TODO:今のステージの画像を二つくっつける
        # embed.set_thumbnail(url="https://app.splatoon2.nintendo.net/images/stage/132327c819abf2bd44d0adc0f4a21aad9cc84bb2.png")

        return msgList
    else:
        raise Exception("BAD STATUS")
