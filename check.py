import time
import re
import getList

# get check List
lists = getList.getList()
lists_cnt = len(lists)
print lists_cnt
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

    offset = 1
    if cnt < offset:
        offset = cnt

    for i in range(cnt-offset, cnt):
        if lines[i] != lines[cnt-1]:
            flag = False

#if flag == False:
#    execfile("",{})
