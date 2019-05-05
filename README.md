# DiscordBot
元K研のSlackのチャンネルで一部活躍していたブキチbot


# 使用技術(後学のため)
* python(3.6.5)
    * python-dotenv
    * discord.py(1.0.0a)

* AWS EC2
# 使用方法(忘れないように)
1. EC2に'ssh discord'で接続する。
1. EC2内で'python main.py &'でバックグランド実行  
    1. 終了の際は'ps x'でプロセスIDを確認した後に'kill ID'する
# コマンド
* `/gachi` …現在+4回分のガチマッチステージ情報を表示
    * `ガチ`は普段の会話の中でBotが誤作動する可能性があるので実装を見送り
* `/league /leag`…現在+4回分のリーグマッチ情報を表示
* `/regular /reg`…現在+4回分のレギュラーマッチ情報を表示
* `/help`…コマンドの使用方法を表示
* `/info`…Botの情報を表示
* `/sake /shake /salmon`…現在サーモンランが開催中か、また直近はいつか


# TODO

* Splatoon2のAPIを引っ張り、ステージ情報を受け取れるようになりたい
    * `/stage`…2回分のレギュラー、ガチ、リグマ情報
* `/ran 2 or 4`…ランダムに人数分武器を割り当てる(各武器種から1つずつ)
* `/hran 2 or 4`…ランダムに人数分武器を割り当てる(武器種関係なし)


* プロセスKillと再実行シェルスクリプトにまとめ、CodeDeploy中で行えるようになりたい
* CodeDeployを用いて、Pushすると自動的にデプロイが行われるようにする

# 備考

## EC2の中身関連
* CodeDeployのHookで永続実行させたい場合は単純に"&"をつけるだけではいけない
   * `~/.pyenv/shims/python main.py > /dev/null 2> /dev/null < /dev/null &`という形で行う。
   * https://docs.aws.amazon.com/ja_jp/codedeploy/latest/userguide/troubleshooting-deployments.html#troubleshooting-deployments-lifecycle-event-failures
* kill -SIGKILLが使えない
    * pkill -KILL -f "python main.py"を使った
* hook用のスクリプトファイルには`chmod +x`をする必要があるが、CodeDeploy Agent側で自動的にchmodしてくれる
    * ログファイルにおいてもWARNなのでそんなに気にしなくていい、HOOKの実行結果は/opt/codedeploy-agent/deployment-root/deployment-logs/*のほうが詳しい