#!/usr/bin/python2.7

import sys
try:
    from crontab import CronTab
except ImportError:
    print ":)pip install python-crontab may help ^_^"
    sys.exit(1)

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Handle the crons")

    parser.add_argument("cronname", help="the name of the cron to be handled")

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--list', action="store_true", help="describe the crons")
    group.add_argument('--start', action="store_true", help="start the cron")
    group.add_argument('--stop', action="store_true", help="stop the cron")

    args = parser.parse_args()


    cron = CronTab()
    iter = cron.find_command(args.cronname)


    if args.list:
        for job in iter:
            print job.is_valid()
            print job
    if args.stop:
        for job in iter:
            if job.is_enabled():
                job.enable(False)
                print "a job disabled"

    if args.start:
        for job in iter:
            if not job.is_enabled():
                job.enable()
                print "a job enabled"

    cron.write()

if __name__ == "__main__":
    main()
