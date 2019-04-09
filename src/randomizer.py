import original_exc
import random
# embedを生成する際に使用するフォーマッタ
# msgListには日時→ルール→ステージの順番で情報が格納されていることが前提

NO_MEMBER_ERROR_MESSAGE = "ボイスチャンネルに誰もいないでし！！！"


# {key: 順番, values:メンバー名}の辞書リストを返却する
def get_random_order(channel_members):
    member_count = len(channel_members)
    if (member_count == 0):
        # ボイチャにメンバーがいない場合、エラーを投げる
        raise original_exc.NoMemberInVoiceChannelException(
            NO_MEMBER_ERROR_MESSAGE)
    else:
        randomizer = random.sample(range(1, member_count + 1), k=member_count)
        member_dct = {}
        counter = 0
        # Dictのリストに[順番、メンバー名]のように格納
        for member in channel_members:
            member_dct[randomizer[counter]] = member.name
            counter += 1

        # 昇順に表示するようソート
        member_dct = sorted(member_dct.items())
    return member_dct
