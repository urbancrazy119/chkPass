# coding : utf-8
import requests
import hashlib
import time
import sys
import re
import getList
reload(sys)
sys.setdefaultencoding('utf-8')

# get check list
lines = getList.getList()

cnt = len(lines)
i = 0

while i < cnt:
    chkList = re.split(r'[\s]',lines[i])
    i += 1
    with requests.Session() as c:
        URL = chkList[1]

        html = c.get(URL)
        t = html.text


        m = hashlib.md5(html.text)
        now = time.localtime()
        file = open("/usr/script/chkPass/log/md5_%s_%04d-%02d-%02d.log"%(chkList[0],now.tm_year, now.tm_mon, now.tm_mday),'a')

        print >> file, m.hexdigest()
        file.close()

execfile("/usr/script/chkPass/check.py",{})

    
