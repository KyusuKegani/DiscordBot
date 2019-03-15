import datetime

DATE_FORMAT = '%Y-%m-%dT%H:%M:%S'
MESSAGE_FORMAT_SAME_DAY = """** {0}/{1} {2}時 - {3}時 **"""
MESSAGE_FORMAT_DIFFERENT_DAY = """** {0}/{1} {2}時 - {3}/{4} {5}時 **"""
MESSAGE_FORMAT_RULE = """{0}"""
MESSAGE_FORMAT_STAGE = """{0},{1}"""


def embedformat(embed, msgList):
    index = 0
    for msg in msgList:
        if (index % 3 == 0):
            embed.add_field(
                name="---------------------------", value=msg, inline=False)
        elif (index % 3 == 1):
            embed.add_field(name="ルール", value=msg, inline=True)
        elif (index % 3 == 2):
            embed.add_field(name="ステージ", value=msg, inline=True)
        index += 1
    return embed


# JSONの一部分を文字列に整形してそのリストを返す関数
def stageformat(jsonlist, repeat=4):
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
