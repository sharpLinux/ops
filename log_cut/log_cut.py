#!/usr/bin/python2.7
#-*- coding: utf-8 -*-
# do: cut the first 1000 lines into new file
# bugs:  accsess.log 一直有写入，而运行该脚本时候需要读写改文件，如何单次脚本执行时间长的话，可能会造成文件被重写，丢失部分数据


import time
from datetime import datetime
def main():
    with open('access.log', 'r') as f:
        lines = f.read().split('\n')
    num = 5
    new_file = 'access_' + datetime.now().isoformat() + '.log'
    print "new file"
    with open (new_file, 'w') as f:
        for line in lines[:num]:
            f.write(line)
    print "ori"
    with open ('access.log', 'w') as f:
        for line in lines[num:-1]:
            f.write(line)
            f.write('\n')



if __name__ == "__main__":
    main()
