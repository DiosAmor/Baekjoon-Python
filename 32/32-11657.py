import sys
input = sys.stdin.readline

inf = sys.maxsize

N,M = map(int,input().split())
graph = []
for _ in range(M):
    A,B,C = map(int,input().split())
    graph.append([A,B,C])

dis = [inf]*(N+1)
def bellmanford(start):
    dis[start] = 0
    for i in range(N):
        for j in range(M):
            cur_node = graph[j][0]
            next_node = graph[j][1]
            c = graph[j][2]
            if dis[cur_node] != inf and dis[next_node] > dis[cur_node] + c:
                dis[next_node] = dis[cur_node] + c
                if i == N-1:
                    return True
    return False

if bellmanford(1):
    print("-1")
else:
    for i in range(2,N+1):
        if dis[i] == inf:
            print("-1")
        else:
            print(dis[i])
            