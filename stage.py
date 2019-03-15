import requests
import json
import formatter

STATUS_OK = 200


def getstage(rule):
    # 非公式API: https://spla2.yuu26.com/
    url_now = 'https://spla2.yuu26.com/{0}/now'.format(rule)
    url_next = 'https://spla2.yuu26.com/{0}/next_all'.format(rule)
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

        # stageformatを用いて現在のステージから1つを取得
        msgList.extend(formatter.stageformat(lists_now["result"], 1))
        # stageformatを用いてこれからのステージから4つ分を取得
        msgList.extend(formatter.stageformat(lists_next["result"], 4))

        # TODO:今のステージの画像を二つくっつける
        # embed.set_thumbnail(url="https://app.splatoon2.nintendo.net/images/stage/132327c819abf2bd44d0adc0f4a21aad9cc84bb2.png")

        return msgList
    else:
        raise Exception("BAD STATUS")
