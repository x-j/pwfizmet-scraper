# credit to https://stackoverflow.com/a/62503751

import schedule
import time
import os
import argparse
import logging

# TODO: logger

class Scheduler:

    def __init__(self, command):
        self.command = command
        print(time.strftime('%Y-%m-%d %T [scheduler]', time.localtime()), 'Scheduler initialised.')
        schedule.every(3).minutes.do(lambda: os.system(command))

    def run(self):
        print(time.strftime('%Y-%m-%d %T [scheduler]', time.localtime()), "Initial run...")
        os.system(self.command)
        while True:
            schedule.run_pending()
            # schedule.get_jobs() # TODO: learn this
            timeout = 60
            
            print(time.strftime('%Y-%m-%d %T [scheduler]', time.localtime()),"Sleeping for",timeout,"s")
            time.sleep(timeout)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scheduler')
    parser.add_argument('command', type=str, help='OS command to be scheduled')

    args = vars(parser.parse_args())
    Scheduler(command = args['command']).run()
