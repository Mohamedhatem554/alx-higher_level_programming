#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "" or sentence is None:
        r2 = None
        r1 = 0
        return (r1, r2)
    r2 = sentence[0]
    r1 = len(sentence)
    return (r1, r2)
