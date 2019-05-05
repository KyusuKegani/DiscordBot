# 指定チャンネルにメンバーがいない時の例外
class NoMemberInVoiceChannelException(Exception):
    def __init__(self, message):
        self.message = message

# OKレスポンス以外が帰ってきたときの例外
class BadStatusException(Exception):
    def __init__(self, message):
        self.message = message
