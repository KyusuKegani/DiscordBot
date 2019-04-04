#!/bin/sh

pkill -KILL -f "python main.py"
cd /home/ec2-user/discord/DiscordBot/
~/.pyenv/shims/python main.py > /dev/null 2> /dev/null < /dev/null &
