#!/bin/sh

pkill -SIGKILL -f 'python ../main.py'
python ../main.py &