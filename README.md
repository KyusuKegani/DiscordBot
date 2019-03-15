# DiscordBot
元K研のSlackのチャンネルで一部活躍していたブキチbot


# 使用技術(後学のため)
* python(3.6.5)
    * python-dotenv
    * discord.py
* AWS EC2
# 使用方法(忘れないように)
1. EC2に'ssh discord'で接続する。
1. EC2内で'python main.py &'でバックグランド実行  
    1. 終了の際は'ps x'でプロセスIDを確認した後に'kill ID'する
# DONE
* gachi/gati/ガチマ/~~ガチ~~ …4回分のガチマッチステージ情報
    * `ガチ`は普段の会話の中でBotが誤作動する可能性があるので未実装
# TODO
* Splatoon2のAPIを引っ張り、ステージ情報を受け取れるようになりたい
    * league/リーグ/リグマ…4回分のリーグマッチ情報
    * stage/ステージ…4回分の塗り、ガチま、リグマ情報
    * sake/salmon/サケ/サーモン…現在サーモンランが開催中か、また直近はいつか

* プロセスKillと再実行シェルスクリプトにまとめ、CodeDeploy中で行えるようになりたい
* CodeDeployを用いて、Pushすると自動的にデプロイが行われるようにする