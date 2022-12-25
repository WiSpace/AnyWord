# standart lib

import awcon

__awc__ = awcon.__awc__
__awvar__ = awcon.__awvar__

@awcon.awfun(["say"])
def say(*text):
    print(*text)
