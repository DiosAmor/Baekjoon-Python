from collections import deque

N,K = map(int,input().split())
visit = [0]*100001

def bfs(X):
    global K
    layer = deque([X])
    while layer:
        X = layer.popleft()
        if X == K:
            return visit[X]
        for i in [X-1,X+1,2*X]:
            if 0<=i<100001 and not visit[i]:
                visit[i] = visit[X] + 1
                layer.append(i)
                
print(bfs(N))            