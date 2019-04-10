import original_exc
import random

# ボイスチャンネルに番号を割り振るためのモジュール

NO_MEMBER_ERROR_MESSAGE = "ボイスチャンネルに誰もいないでし！！！"


# {key: 順番, values:メンバー名}の辞書リストを返却する
def get_random_order(channel_members):
    member_count = len(channel_members)
    if (member_count == 0):
        # ボイチャにメンバーがいない場合、エラーを投げる
        raise original_exc.NoMemberInVoiceChannelException(
            NO_MEMBER_ERROR_MESSAGE)
    else:
        randomizer = random.sample(range(0, member_count), k=member_count)
        member_dct = {}
        counter = 0
        # Dictのリストに[順番、メンバー名]のように格納
        for member in channel_members:
            # ここでOut of boundsとなるため、0-indexedで行なっている
            # mainの呼び出しのところで1-indexedに変換
            member_dct[randomizer[counter]] = member.name
            counter += 1

        # 昇順に表示するようソート
        member_dct = sorted(member_dct.items())
    return member_dct
