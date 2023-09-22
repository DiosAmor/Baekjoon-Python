#pypy

import sys
input = sys.stdin.readline

N = int(input())
score = [list(map(int,input().split())) for _ in range(N)]

lst_total = []
lst = []
def dfs(N):
    if len(lst) == N//2:
        lst_total.append(list(lst))
        return
    else:
        for i in range(N):
            if i not in lst:
                if len(lst) > 0 and i < lst[-1]:
                    pass
                else:
                    lst.append(i)
                    dfs(N)
                    lst.pop()
                
dfs(N)

min_value = 20*100
for i in range(len(lst_total)):
    temp = 0
    for j in range(N//2):
        for k in range(N//2):
            temp += score[lst_total[i][j]][lst_total[i][k]]
    
    temp2 = 0
    lst2 = set(range(N)) - set(lst_total[i])
    lst2 = list(lst2)
    for j in range(N//2):
        for k in range(N//2):
            temp2 += score[lst2[j]][lst2[k]]
    
    diff = abs(temp-temp2)
    if diff < min_value:
        min_value = diff
        
print(min_value)