n = int(input())

dp = [0]*n
number = [0]*n
for i in range(n):
    number[i] = int(input())
    if i == 0:
        dp[0] = number[0]
    elif i == 1:
        dp[1] = number[0] + number[1]
    elif i == 2:
        temp1 = number[i]+number[i-1]
        temp2 = number[i]+dp[i-2]
        temp3 = dp[i-1]
        dp[i] = max(temp1,temp2,temp3)
    else:
        temp1 = number[i]+number[i-1]+dp[i-3]
        temp2 = number[i]+dp[i-2]
        temp3 = dp[i-1]
        dp[i] = max(temp1,temp2,temp3)
print(dp[n-1])