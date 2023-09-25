#pypy

import sys
input = sys.stdin.readline

N = int(input())

matrix = []
for _ in range(N):
    matrix.append(list(map(int,input().split())))

dp = [[0]*(N) for _ in range(N)]

for i in range(N):
    for j in range(i+1,N):
        if j == i + 1:
            dp[i][j] = matrix[i][0] * matrix[i][1] * matrix[j][1]
for i in range(N-2,-1,-1):
    for j in range(i+1,N):
        if dp[i][j] == 0:
            dp[i][j] = min([dp[i][k]+dp[k+1][j]+matrix[i][0]*matrix[k][1]*matrix[j][1] for k in range(i,j)])
print(dp[0][N-1])            