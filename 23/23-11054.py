n = int(input())
numbers = list(map(int,input().split()))

dp = [1]*n
for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i],dp[j]+1)

numbers.reverse()
dp_reverse = [1]*n
for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp_reverse[i] = max(dp_reverse[i],dp_reverse[j]+1)

dp_total = []
for i in range(n):
    dp_total.append(dp_reverse[i]+dp[n-i-1]-1)
print(max(dp_total))