# This file is placed in the Public Domain.


"uptime"


import time


from objr.command import STARTTIME
from objr.utility import elapsed


def upt(event):
    event.reply(elapsed(time.time()-STARTTIME))
