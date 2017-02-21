#-*- coding: utf-8 -*-
import time
import re
import getList
import sendMsg

# get check List
lists = getList.getList()
lists_cnt = len(lists)
i = 0

while i < lists_cnt:
    chkList = re.split(r'[\s]',lists[i])
    i += 1
    now = time.localtime()

    file = open("/usr/script/chkPass/log/md5_%s_%04d-%02d-%02d.log"%(chkList[0], now.tm_year, now.tm_mon, now.tm_mday),'r')
    lines = file.readlines()
    file.close()

    flag = True

    cnt = len(lines)

    # set compare res
    offset = 2 
    if cnt < offset:
        offset = cnt

    # compare hash value
    for j in range(cnt-offset, cnt):
        if lines[j] != lines[cnt-1]:
            flag = False

    # if unmatch
    if flag == False:
        # send msg
        for z in range(2, len(chkList)):
            sendMsg.send_msg_to_telegram(chkList[z],'['+chkList[0]+'] 변화 감지 : \t'+chkList[1])
