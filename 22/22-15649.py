N,M = map(int,input().split())

lst = []
def dfs(N,M):
    if len(lst) == M:
        for i in lst:
            print(i,end = " ")
        print()
        return
    else:
        for i in range(1,N+1):
            if i not in lst:
                lst.append(i)
                dfs(N,M)
                lst.pop()

dfs(N,M)