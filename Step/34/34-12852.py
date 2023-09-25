from collections import deque
import sys
inf = sys.maxsize

N = int(input())
dp = [inf]*(N+1)
dp[N] = 0

layer = deque([[N,0,[N]]])
while layer:
    queue = []
    x,cnt,queue = layer.popleft()
    if x == 1:
        print(cnt)
        print(*queue,sep=" ")
        break
    else:
        if x % 3 == 0:
            nx = x//3
            if dp[nx] > cnt+1:
                dp[nx] = cnt+1
                temp1 = list(queue)
                temp1.append(nx)
                layer.append([nx, cnt+1,temp1])
        if x % 2 == 0:
            nx = x//2
            if dp[nx] > cnt+1:
                dp[nx] = cnt+1
                temp2 = list(queue)
                temp2.append(nx)
                layer.append([nx, cnt+1,temp2])
        nx = x-1
        if dp[nx] > cnt+1:
                dp[nx] = cnt+1
                temp3 = list(queue)
                temp3.append(nx)
                layer.append([nx, cnt+1,temp3])