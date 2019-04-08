# 指定チャンネルにメンバーがいない時の例外
class NoMemberInVoiceChannelException(Exception):
    def __init__(self, message):
        self.message = message
