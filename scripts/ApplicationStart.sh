#!/bin/sh

pkill -SIGKILL -f 'python ../main.py'
~/.pyenv/shims/python ../main.py &
