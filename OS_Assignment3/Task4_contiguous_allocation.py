#!/usr/bin/env python3
def alloc(strategy,parts,procs):
    p=parts.copy(); a=[-1]*len(procs)
    for i,ps in enumerate(procs):
        idx=-1
        if strategy=='first':
            for j,x in enumerate(p):
                if x>=ps: idx=j; break
        elif strategy=='best':
            best=None
            for j,x in enumerate(p):
                if x>=ps and (best is None or x<p[best]): best=j
            idx=best
        else:
            worst=None
            for j,x in enumerate(p):
                if x>=ps and (worst is None or x>p[worst]): worst=j
            idx=worst
        if idx!=None and idx!=-1: a[i]=idx; p[idx]-=ps
    print(a)
if __name__=='__main__':
    parts=list(map(int,input().split()))
    procs=list(map(int,input().split()))
    alloc('first',parts,procs)
    alloc('best',parts,procs)
    alloc('worst',parts,procs)
