N,K = map(int,input().split())
temp = list(map(int,input().split()))

dp = [0]*(N-K+1)

for i in range(len(dp)):
    if i == 0:
        for j in range(K):
            dp[i] += temp[i+j]
    else:
        dp[i] = dp[i-1] + temp[i+K-1] - temp[i-1]
print(max(dp))