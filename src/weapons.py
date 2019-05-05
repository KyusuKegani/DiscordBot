import requests
import json
import original_exc

STATUS_OK = 200
USER_AGENT = "Discord Bukichi Bot/v1.1 (twitter @bser_assistant)"


def get_weapon():
    # 非公式APIの　https://github.com/fetus-hina/stat.ink/tree/master のURL
    url = 'https://stat.ink/api/v2/weapon'

    # 念の為User_Agentを偽装
    headers = {'User-Agent': USER_AGENT}
    res = requests.get(url, headers=headers)

    # ステイタスコードがOKであることを確認
    if (res.status_code == STATUS_OK):
        weapon_list = json.loads(res.text)
        return weapon_list
    else:
        raise original_exc.BadStatusException("BAD STATUS")
