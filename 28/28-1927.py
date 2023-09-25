import sys
import heapq

input = sys.stdin.readline
heap = []
N = int(input())
for _ in range(N):
    temp = int(input())
    if temp == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,temp)