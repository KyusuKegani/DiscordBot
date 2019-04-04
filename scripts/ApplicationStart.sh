#!/bin/sh

pkill -KILL -f "python3 main.py"
cd /home/ec2-user/discord/DiscordBot/
python3 main.py &
