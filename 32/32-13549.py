from heapq import heappush, heappop
import sys

max_N = 100000
inf = sys.maxsize
N,K = map(int,input().split())
time = [inf]*(max_N+1)
heap = []

if N >= K:
    print(N-K)
else:
    heappush(heap,[0,N])
    while heap:
        t,x = heappop(heap)
        for nx in [x-1,x+1,2*x]:
            if 0<=nx<=max_N:
                if time[nx] == inf:
                    if nx == 2*x:
                        time[nx] = t
                    else:
                        time[nx] = t+1
                    heappush(heap,[time[nx],nx])
    print(time[K])

