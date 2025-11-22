#!/usr/bin/env python3
def indexed_allocation():
    total=int(input()); blk=[0]*total
    n=int(input())
    for i in range(n):
        idx=int(input())
        if idx>=total or blk[idx]==1: print("Invalid"); continue
        c=int(input()); data=list(map(int,input().split()))
        if any(b>=total or blk[b]==1 for b in data): print("Invalid"); continue
        blk[idx]=1
        for b in data: blk[b]=1
        print("Allocated",i+1)
if __name__=='__main__': indexed_allocation()
