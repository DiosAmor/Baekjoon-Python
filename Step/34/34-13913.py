from collections import deque

N,K = map(int,input().split())
visit = [0]*100001
stamp = [0]*100001


layer = deque([N])
while layer:
    x = layer.popleft()
    if x == K:
        print(visit[x])
        result = [x]
        for _ in range(visit[x]):
            x = stamp[x]
            result.append(x)
        result.reverse()
        print(*result)
        break
    for i in [x-1,x+1,2*x]:
        if 0<=i<100001 and not visit[i]:
            layer.append(i)
            visit[i] = visit[x]+1
            stamp[i] = x