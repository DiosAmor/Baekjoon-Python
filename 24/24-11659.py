import sys
input = sys.stdin.readline

N,M = map(int,input().split())
numbers = list(map(int,input().split()))

dp = [0]*(N+1)
dp[1] = numbers[0]
for i in range(2,N+1):
    dp[i] = dp[i-1] + numbers[i-1]
for _ in range(M):
    i,j = map(int,input().split())
    result = dp[j]-dp[i-1]
    print(result)
    