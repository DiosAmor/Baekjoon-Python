#pypy

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
dp = [[0]*N for _ in range(N)]

for i in range(N):
    numbers = list(map(int,input().split()))
    dp[i][0] = numbers[0]
    for j in range(1,N):
        dp[i][j] = dp[i][j-1] + numbers[j]
for k in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    x1 -= 1
    y1 -= 1
    y2 -= 1
    temp=0
    for l in range(x1,x2):
        if y1 > 0:
            temp += dp[l][y2] - dp[l][y1-1]
        else:
            temp += dp[l][y2]
    print(temp)