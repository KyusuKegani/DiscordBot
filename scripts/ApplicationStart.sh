#!/bin/sh

pkill -KILL -f "python src/main.py"
cd /home/ec2-user/discord/DiscordBot/
~/.pyenv/shims/python src/main.py > /dev/null 2> /dev/null < /dev/null &
