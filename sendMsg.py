#-*- coding: utf-8 -*-
import os

def send_msg_to_telegram(username, msg):
    send_cmd = '(echo "msg %s %s";) |nc localhost 8123 -q 3'%( username, msg)

    os.system(send_cmd)

