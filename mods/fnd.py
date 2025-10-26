# This file is placed in the Public Domain.


"find"


import time


from objr.command import elapsed
from objr.methods import fmt
from objr.persist import find, fntime, skel, store, types


def fnd(event):
    skel(store())
    if not event.rest:
        res = sorted([x.split('.')[-1].lower() for x in types(store())])
        if res:
            event.reply(",".join(res))
        else:
            event.reply("no data yet.")
        return
    otype = event.args[0]
    nmr = 0
    for fnm, obj in list(find(store(), otype, event.gets)):
        event.reply(f"{nmr} {fmt(obj)} {elapsed(time.time()-fntime(fnm))}")
        nmr += 1
    if not nmr:
        event.reply("no result")
