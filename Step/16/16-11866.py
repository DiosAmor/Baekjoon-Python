from collections import deque

N,K = map(int,input().split())

que = deque(range(1,N+1))
result = []

while que:
    for i in range(K-1):
        que.append(que.popleft())
    result.append(que.popleft())
print("<",end="")
for i in range(N-1):
    print(result[i],end=", ")
print(result[N-1],end="")
print('>')