#!/usr/bin/python2.7
import psutil
import time
def main():
  while True:
    print psutil.cpu_percent()
    print psutil.cpu_times()
    print psutil.disk_usage()
    time.sleep(20)

if __name__ == '__main__':
  main()
