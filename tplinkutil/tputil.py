#!/usr/bin/python3
import sys
import time

from tplinkutil import logger
from tplinkutil.modes import Mode


class TPUtil(object):
    def __init__(self, mode: Mode):
        self.mode = mode

    def run(self):
        logger.info('Starting TPUtil in mode %s with timestep %f' % (self.mode.getname(), self.mode.timestep))
        # main loop
        while True:
            try:
                self.mode()
                logger.debug('Tick')
                time.sleep(self.mode.timestep)
            except KeyboardInterrupt:
                logger.info('Shutting down...')
                break

        sys.exit(0)