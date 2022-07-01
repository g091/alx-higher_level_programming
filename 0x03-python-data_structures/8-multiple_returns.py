#!/usr/bin/python3
def multiple_returns(sentence):
    t = ()
    if len(sentence) == 0:
        t = 0, None
        return t
    else:
        t = len(sentence), sentence[0]
        return t
