import unittest
import mock
import src.randomizer as rm
import src.original_exc as exc


# 'python -m unittest *.py'で実行することができる
class TestFormatter(unittest.TestCase):
    # 複数人チャンネルいた場合のテスト
    @mock.patch('random.sample')
    def test_get_random_order(self, random_call):
        A = mock.MagicMock(name="A")
        B = mock.MagicMock(name="B")
        C = mock.MagicMock(name="C")
        D = mock.MagicMock(name="D")
        E = mock.MagicMock(name="E")

        channel_members = [A, B, C, D, E]
        random_call.return_value = [3, 4, 5, 2, 1]
        member_dct = rm.get_random_order(channel_members)
        self.assertEqual([(1, E.name), (2, D.name), (3, A.name), (4, B.name),
                          (5, C.name)], member_dct)

    # 一人しかチャンネルいた場合のテスト
    def test_get_random_order_single(self):
        A = mock.MagicMock(name="A")

        channel_members = [A]
        member_dct = rm.get_random_order(channel_members)
        self.assertEqual([(1, A.name)], member_dct)

    # 誰もチャンネルいない場合のテスト
    def test_get_random_order_exception(self):
        channel_members = []
        with self.assertRaises(exc.NoMemberInVoiceChannelException):
            rm.get_random_order(channel_members)
        