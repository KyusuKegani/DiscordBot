#!/bin/sh

kill -SIGKILL -f 'python main.py'
cd /home/ec2-user/discord/DiscordBot/
python main.py &
