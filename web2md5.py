# coding : utf-8
import requests
import hashlib
import time
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')

# get check list
chk_file = open("/usr/script/chkPass/chklist.txt",'r')
lines = chk_file.readlines()
chk_file.close()

cnt = len(lines)
i = 0

while i < cnt:
    l = re.split(r'[\s]',lines[i])
    i += 1

print l

with requests.Session() as c:
    URL = l[1]

    html = c.get(URL)
    t = html.text


    m = hashlib.md5(html.text)
    now = time.localtime()
    file = open("/usr/script/chkPass/log/md5_%s_%04d-%02d-%02d.log"%(l[0],now.tm_year, now.tm_mon, now.tm_mday),'a')

    print >> file, m.hexdigest()
    file.close()

execfile("/usr/script/chkPass/check.py",{})

    
