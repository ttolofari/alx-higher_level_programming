#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    fst_char = sentence[0] if length > 0 else "None"
    tup = length, fst_char
    return(tup)
