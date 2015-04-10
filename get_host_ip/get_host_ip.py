#!/usr/bin/python2.7
import os
def get_host_ip():
  result = {}
  sys_tmp = os.popen('LANG=en ifconfig').readlines()
  for i in range(len(sys_tmp)):
    list_tmp = sys_tmp[i].split()
    for j in range(len(list_tmp)):
      if list_tmp[j].find('eth') == 0:
	result[list_tmp[j]] = sys_tmp[i+1].split()[1].split(':')[1]
	break  
  return result
def main():
  host_ip = get_host_ip()
  print host_ip
if __name__ == "__main__":
  main()
