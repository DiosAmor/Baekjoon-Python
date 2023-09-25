N = int(input())
dp = [list(map(int,input().split()))]

for i in range(N-1):
    a,b,c = map(int,input().split())
    temp1 = a+min(dp[i][1],dp[i][2])
    temp2 = b+min(dp[i][0],dp[i][2])
    temp3 = c+min(dp[i][0],dp[i][1])
    dp.append([temp1,temp2,temp3])

print(min(dp[N-1]))