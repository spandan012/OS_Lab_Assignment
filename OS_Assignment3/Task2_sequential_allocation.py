#!/usr/bin/env python3
def sequential_allocation():
    total=int(input()); blk=[0]*total
    n=int(input())
    for i in range(n):
        s=int(input()); l=int(input())
        ok=True
        for j in range(s,s+l):
            if j>=total or blk[j]==1: ok=False; break
        if ok:
            for j in range(s,s+l): blk[j]=1
            print("Allocated",i+1)
        else: print("Cannot allocate",i+1)
if __name__=='__main__': sequential_allocation()
