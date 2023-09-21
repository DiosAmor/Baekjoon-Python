import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

que = deque()
que_size = 0
for _ in range(N):
    order = list(input().split())
    if order[0] == 'push':
        que.append(order[1])
        que_size += 1
    if order[0] == 'front':
        if que_size > 0:
            print(que[0])
        else:
            print(-1)
    if order[0] == 'back':
        if que_size > 0:
            print(que[-1])
        else:
            print(-1)
    if order[0] == 'size':
        print(que_size)
    if order[0] == 'empty':
        if que_size > 0:
            print(0)
        else:
            print(1)
    if order[0] == 'pop':
        if que_size > 0:
            print(que.popleft())
            que_size -= 1
        else:
            print(-1)