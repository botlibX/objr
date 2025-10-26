# This file is placed in the Public Domain.


"uptime"


import time


from objr.command import elapsed


STARTTIME = time.time()


def upt(event):
    event.reply(elapsed(time.time()-STARTTIME))
