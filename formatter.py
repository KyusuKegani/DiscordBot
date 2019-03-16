import datetime

DATE_FORMAT = '%Y-%m-%dT%H:%M:%S'
MESSAGE_FORMAT_SAME_DAY = """** {0}/{1} {2}時 - {3}時 **"""
MESSAGE_FORMAT_DIFFERENT_DAY = """** {0}/{1} {2}時 - {3}/{4} {5}時 **"""
MESSAGE_FORMAT_RULE = """{0}"""
MESSAGE_FORMAT_STAGE = """{0},{1}"""

SALMON_FORMAT_STAGE = """{0}"""
SALMON_FORMAT_STAGE_IMAGE = """{0}"""
SALMON_FORMAT_WEAPON = """{0},{1},{2},{3}"""

SLASH = "------------------------------------------------------------------"


# embedを生成する際に使用するフォーマッタ
# msgListには日時→ルール→ステージの順番で情報が格納されていることが前提
def stage_embed_format(embed, msgList):
    index = 0
    for msg in msgList:
        if (index % 3 == 0):
            embed.add_field(name=SLASH, value=msg, inline=False)
        elif (index % 3 == 1):
            embed.add_field(name="ルール", value=msg, inline=True)
        elif (index % 3 == 2):
            embed.add_field(name="ステージ", value=msg, inline=True)
        index += 1
    return embed


# サーモンラン用のembedを生成する際に使用するフォーマッタ
# msgListには日時→ステージ名→ステージ画像のURL→ブキの名前の順番で情報が格納されていることが前提
def salmon_embed_format(embed, msgList):
    index = 0
    # 現在開催中ならタイトルに「開催中！！！！」を追加

    for msg in msgList:
        if (index % 4 == 0):
            embed.add_field(name=SLASH, value=msg, inline=False)
        elif (index % 4 == 1):
            if (len(msg) != 0):
                # msgが空文字列ならフィールドはスキップ
                embed.add_field(name="ステージ", value=msg, inline=True)
        elif (index % 4 == 2):
            if (index == 2):
                # サムネイルは直近の予定のみにする
                embed.set_thumbnail(url=msg)
        elif (index % 4 == 3):
            if (len(msg) != 0):
                # msgが空文字列ならフィールドはスキップ
                embed.add_field(name="ブキ", value=msg, inline=True)
        index += 1
    return embed


# JSONを受け取り、ステージ情報に整形し、そのリストを返す関数
# 日付→ルール→ステージの順で格納されている
def stage_format(jsonlist, repeat=4):
    stageList = []
    for list in jsonlist:
        # repeatで指定された分ののステージ情報のみ表示
        if (jsonlist.index(list) >= repeat):
            break

        # Python 3.6.5(<3.7.0)のため、fromisoformatは使用していない
        startdt = datetime.datetime.strptime(list["start"], DATE_FORMAT)
        enddt = datetime.datetime.strptime(list["end"], DATE_FORMAT)

        # 同じ日かによってフォーマットを変更
        if (startdt.day == enddt.day):
            # Ex.”3/15 19時 - 21時”
            stageList.append(
                MESSAGE_FORMAT_SAME_DAY.format(startdt.month, startdt.day,
                                               startdt.hour, enddt.hour))
        else:
            # Ex.”3/15 23時 - 3/16 1時”
            stageList.append(
                MESSAGE_FORMAT_DIFFERENT_DAY.format(startdt.month, startdt.day,
                                                    startdt.hour, enddt.month,
                                                    enddt.day, enddt.hour))

        stageList.append(MESSAGE_FORMAT_RULE.format(list["rule_ex"]["name"]))
        stageList.append(
            MESSAGE_FORMAT_STAGE.format(list["maps_ex"][0]["name"],
                                        list["maps_ex"][1]["name"]))
    return stageList


# JSONの一部を受け取り、サーモンランの形式に乗っ取って返す関数
# 日時→ステージ名→ステージ画像のURL(ないなら空文字列)→ブキの名前(ないなら空文字列)の順に格納
def salmon_format(jsonlist):
    salmonList = []
    for list in jsonlist:

        # Python 3.6.5(<3.7.0)のため、fromisoformatは使用していない
        startdt = datetime.datetime.strptime(list["start"], DATE_FORMAT)
        enddt = datetime.datetime.strptime(list["end"], DATE_FORMAT)
        append_string = "(現在開催中！！！！)"
        # 同じ日かによってフォーマットを変更
        if (startdt.day == enddt.day):
            # Ex.”3/15 19時 - 21時”
            day_msg = MESSAGE_FORMAT_SAME_DAY.format(
                startdt.month, startdt.day, startdt.hour, enddt.hour)
        else:
            # Ex.”3/15 23時 - 3/16 1時”
            day_msg = MESSAGE_FORMAT_DIFFERENT_DAY.format(
                startdt.month, startdt.day,
                startdt.hour, enddt.month,
                enddt.day, enddt.hour)

        # 開催中なら開催中の文字列を追加する
        if(startdt <= datetime.datetime.now() <= enddt):
            salmonList.append(day_msg + append_string)
        else:
            salmonList.append(day_msg)

        # APIでは2つ先以上のステージ、ブキはNULLとなるため、その判定
        if (list["stage"] is not None):
            salmonList.append(
                SALMON_FORMAT_STAGE.format(list["stage"]["name"]))
            salmonList.append(
                SALMON_FORMAT_STAGE_IMAGE.format(list["stage"]["image"]))
        else:
            salmonList.append("")
            salmonList.append("")

        if (list["weapons"] is not None):
            salmonList.append(
                SALMON_FORMAT_WEAPON.format(
                    list["weapons"][0]["name"], list["weapons"][1]["name"],
                    list["weapons"][2]["name"], list["weapons"][3]["name"]))
        else:
            salmonList.append("")

    return salmonList
