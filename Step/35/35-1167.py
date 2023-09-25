import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

V = int(input())
tree = [[] for _ in range(V+1)]
for _ in range(V):
    temp = list(map(int,input().split()))
    for i in range(1,len(temp)-2,2):
        tree[temp[0]].append([temp[i],temp[i+1]])

def dfs(node,cost):
    for i,j in tree[node]:
        if visit[i] == 0:
            visit[i] = j+cost
            dfs(i,j+cost)
            
visit = [0]*(V+1)
visit[1] = -1
dfs(1,0)
start = visit.index(max(visit))
visit = [0]*(V+1)
visit[start] = -1

dfs(start,0)
print(max(visit))