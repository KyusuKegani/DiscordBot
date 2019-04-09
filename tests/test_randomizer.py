import unittest
import os
import json
import src.randomizer as rm


# 'python -m unittest *.py'で実行することができる
class TestFormatter(unittest.TestCase):
    # サーモンランのうち、ステージ情報とブキ情報があるパターンのテスト
    def test_salmon_format_with_stage(self):
        base = os.path.dirname(os.path.abspath(__file__))
        path = os.path.normpath(
            os.path.join(base, 'json/salmon_with_stage.json'))
        f = open(path, "r")
        json_list = json.load(f)
        salmon_list = rm.salmon_format(json_list["result"])
        collect_salmon_list = [
            "** 3/16 17時 - 3/18 5時 **", "朽ちた箱舟 ポラリス",
            "https://app.splatoon2.nintendo.net/images/coop_stage/50064ec6e97aac91e70df5fc2cfecf61ad8615fd.png",
            "ノーチラス47,ノヴァブラスター,オーバーフロッシャー,Rブラスターエリート"
        ]
        self.assertEquals(salmon_list, collect_salmon_list)
        f.close()

    # サーモンランのうち、ステージ情報とブキ情報がないパターンのテスト
    def test_salmon_format_without_stage(self):
        base = os.path.dirname(os.path.abspath(__file__))
        path = os.path.normpath(
            os.path.join(base, 'json/salmon_without_stage.json'))
        f = open(path, "r")
        json_list = json.load(f)
        salmon_list = fm.salmon_format(json_list["result"])
        collect_salmon_list = ["** 4/12 21時 - 4/14 15時 **", "", "", ""]
        self.assertEquals(salmon_list, collect_salmon_list)
        f.close()

    # ステージ情報のうち、現在のステージだけのテスト
    def test_stage_format_now(self):
        base = os.path.dirname(os.path.abspath(__file__))
        path = os.path.normpath(
            os.path.join(base, 'json/stage_now_gachi.json'))
        f = open(path, "r")
        json_list = json.load(f)
        stage_list = fm.stage_format(json_list["result"], 1)
        collect_stage_list = [
            "** 4/9 9時 - 11時 **", "ガチホコバトル", "海女美術大学,ガンガゼ野外音楽堂"
        ]
        self.assertEquals(stage_list, collect_stage_list)
        f.close()

    # ステージ情報のうち、これ以降4つのステージのテスト
    def test_stage_format_next_all(self):
        base = os.path.dirname(os.path.abspath(__file__))
        path = os.path.normpath(
            os.path.join(base, 'json/stage_next_all_gachi.json'))
        f = open(path, "r")
        json_list = json.load(f)
        stage_list = fm.stage_format(json_list["result"], 4)
        collect_stage_list = [
            "** 4/9 11時 - 13時 **",
            "ガチヤグラ",
            "ザトウマーケット,チョウザメ造船",
            "** 4/9 13時 - 15時 **",
            "ガチアサリ",
            "タチウオパーキング,フジツボスポーツクラブ",
            "** 4/9 15時 - 17時 **",
            "ガチエリア",
            "アロワナモール,ホッケふ頭",
            "** 4/9 17時 - 19時 **",
            "ガチホコバトル",
            "ショッツル鉱山,モズク農園",
        ]
        self.assertEquals(stage_list, collect_stage_list)
        f.close()