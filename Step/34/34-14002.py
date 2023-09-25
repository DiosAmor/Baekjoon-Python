import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int,input().split()))

dp = [1]*(N)

for i in range(N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i],dp[j]+1)
            
dp_max = max(dp)
print(dp_max)

idx = dp_max
result = []
for i in range(N-1,-1,-1):
    if idx == dp[i] and idx > 0:
        result.append(numbers[i])
        idx -= 1
result.reverse()
print(*result)