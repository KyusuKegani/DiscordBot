import requests
import json
import formatter

STATUS_OK = 200
USER_AGENT = "Discord Bukichi Bot/v1.1 (twitter @bser_assistant)"


def get_random_weapon(number_of_weapons):
    # 非公式APIの https://stat.ink/api/v2/ のURL    
    # https://github.com/fetus-hina/stat.ink/blob/master/doc/api-2/get-weapon.md
    url = 'https://stat.ink/api/v2/weapon'

    # このAPIではUser-Agentの指定はない、一応Botの暴走で怒られるかもしれないので念の為偽装する
    headers = {'User-Agent': USER_AGENT}

    res = requests.get(url, headers=headers)

    msgList = []

    if (res.status_code == STATUS_OK):
        lists = json.loads(res.text)
        # TODO:weapon用のフォーマットを実装する必要がある。今日は疲れた
        msgList.extend(formatter.weapon_format(lists["result"]))
        return msgList
    else:
        raise Exception("BAD STATUS")

