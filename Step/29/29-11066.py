#pypy

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    C = list(map(int,input().split()))
    dp = [[0]*K for _ in range(K)]
    
    for i in range(K):
        for j in range(K):
            if j == i+1:
                dp[i][j] = C[i] + C[j]
    for i in range(K-2,-1,-1):
        for j in range(i+1,K):
            if dp[i][j] == 0:
                dp[i][j] = min([dp[i][k]+dp[k+1][j] for k in range(i,j)]) + sum(C[i:j+1])
    print(dp[0][K-1])
    