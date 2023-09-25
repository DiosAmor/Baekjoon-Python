N,M = map(int,input().split())
m = list(map(int,input().split()))
c = list(map(int,input().split()))

max_cost = sum(c)
dp = [[0]*(max_cost+1) for _ in range(N+1)]

min_cost = max_cost
for i in range(1,N+1):
    temp_memo = m[i-1]
    temp_cost = c[i-1]

    for j in range(1,max_cost+1):
        if j < temp_cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-temp_cost]+temp_memo,dp[i-1][j])
        if dp[i][j] >= M:
            if min_cost > j:
                min_cost = j

print(min_cost)