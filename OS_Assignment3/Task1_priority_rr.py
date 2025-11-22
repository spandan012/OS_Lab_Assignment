#!/usr/bin/env python3
# Priority + RR scheduling
from collections import deque
def priority_scheduling(processes):
    procs = sorted(processes, key=lambda x: x[2])
    wt=0; tw=0; tt=0
    for pid,bt,pr in procs:
        tat=wt+bt; tw+=wt; tt+=tat; wt+=bt
    return tw/len(procs), tt/len(procs)
def round_robin(processes,q):
    from collections import deque
    qd=deque([[pid,bt] for pid,bt in processes])
    rem={pid:bt for pid,bt in processes}
    finish={}; t=0
    while qd:
        pid,bt=qd.popleft()
        ex=min(bt,q); t+=ex; rem[pid]-=ex
        if rem[pid]>0: qd.append([pid,rem[pid]])
        else: finish[pid]=t
    tw=sum(finish[pid]-bt for pid,bt in processes)/len(processes)
    tt=sum(finish[pid] for pid,bt in processes)/len(processes)
    return tw,tt
