# for getting check List 
import os
def getList():
    file = open(os.getcwd()+'/chklist.txt','r')
    lines = file.readlines()
    file.close()
    return lines
