import original_exc
import random
import weapon
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
        weapon_dct = {}
        counter = 0
        # Dictのリストに[順番、メンバー名]のように格納
        for member in channel_members:
            # ここでOut of boundsとなるため、0-indexedで行なっている
            # mainの呼び出しのところで1-indexedに変換
            weapon_dct[randomizer[counter]] = member.name
            counter += 1

        # 昇順に表示するようソート
        weapon_dct = sorted(weapon_dct.items())
    return weapon_dct

# {key: メンバー名, values: ブキ名}の辞書リストを返却する
def get_random_weapon(channel_members):
    member_count = len(channel_members)
    if (member_count == 0):
        # ボイチャにメンバーがいない場合、エラーを投げる
        raise original_exc.NoMemberInVoiceChannelException(
            NO_MEMBER_ERROR_MESSAGE)
    else:
        # get_weaponでAPIから現在のブキの一覧を取得
        weapon_list = weapon.get_weapon()
        randomizer = random.sample(range(0, len(weapon_list)), k=member_count)
        weapon_dct = {}
        counter = 0
        # Dictのリストに[順番、メンバー名]のように格納
        for member in channel_members:
            # ここでOut of boundsとなるため、0-indexedで行なっている
            # mainの呼び出しのところで1-indexedに変換
            weapon_dct[member.name] = weapon_list[randomizer[counter]]["name"]["ja_JP"]
            counter += 1

        # 昇順に表示するようソート
        weapon_dct = sorted(weapon_dct.items())
    return weapon_dct