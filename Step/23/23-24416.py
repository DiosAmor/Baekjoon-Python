#pypy

num = int(input())

count_dfs = 0
def dfs(n):
    global count_dfs
    if n==1 or n==2:
        count_dfs += 1
        return 1
    else:
        return dfs(n-1)+dfs(n-2)

count_dp = 0
memo = [0,1,1]+[0]*(num-2)

def dp(n):
    global count_dp
    if n == 1 or n == 2:
        return memo[n]
    else:
        for i in range(3,n+1):
            count_dp += 1
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]
dfs(num)
dp(num)
print(count_dfs, count_dp)