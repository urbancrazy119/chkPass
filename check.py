import time

now = time.localtime()

file = open("/usr/script/chkPass/log/md5_%04d-%02d-%02d.log"%(now.tm_year, now.tm_mon, now.tm_mday),'r')
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
