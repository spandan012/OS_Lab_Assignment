#!/usr/bin/env python3
def MFT():
    mem=int(input()); ps=int(input()); n=int(input())
    for i in range(n):
        p=int(input())
        if p<=ps: print("Allocated",i+1)
        else: print("Too big",i+1)
def MVT():
    mem=int(input()); n=int(input())
    for i in range(n):
        p=int(input())
        if p<=mem: mem-=p; print("Allocated",i+1)
        else: print("No space",i+1)
if __name__=='__main__':
    MFT(); MVT()
