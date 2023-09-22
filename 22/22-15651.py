N,M = map(int,input().split())


def dfs(N,M,lst):
    if len(lst) == M:
        print(' '.join(map(str,lst)))
        return
    else:
        for i in range(1,N+1):
            lst.append(i)
            dfs(N,M,lst)
            lst.pop()
                
        
dfs(N,M,[])
