import os
def cron_ctrl(arg1,arg2):
  if arg2 == 'start':
    tmp = os.popen('crontab -e').readlines() 
    print tmp
#  if arg1 == 'stop':
  
#  if arg1 == 'list':
  
cron_ctrl('','start')
