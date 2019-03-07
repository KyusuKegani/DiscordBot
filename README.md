# DiscordBot
元K研のSlackのチャンネルで一部活躍していたブキチbot


# 使用技術(後学のため)
* python(3.6.5)
    * python-dotenv
    * discord.py
* AWS EC2
# 使用方法(忘れないように)
1. EC2に'ssh discord'で接続する。
1. EC2内で'nohup python main.py'でバックグランド実行  
    1. 終了の際は'ps x'でプロセスIDを確認した後に'kill ID'する
# TODO
* ブキチ(開発中)の作成、本番デプロイはブキチ(改)で行う
* CodeDeployを用いて、Pushすると自動的にデプロイ＆コマンド実行できるようにする
* プロセスの終了を自動でできるようになりたい