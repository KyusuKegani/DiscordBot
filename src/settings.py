import os
from os.path import join, dirname
from dotenv import load_dotenv
# BOTのトークンを読み込むためのモジュール
# .envはこのファイルと同じ改装に置くこと！！！
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BT = os.environ.get("BOT_TOKEN")
