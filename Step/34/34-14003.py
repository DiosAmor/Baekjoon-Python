from bisect import bisect_left
import sys
input = sys.stdin.readline
inf = sys.maxsize

N = int(input())
numbers = [0] + list(map(int,input().split()))

dp = [0]*(N+1)
result = [-inf]

for i in range(1,N+1):
    if result[-1] < numbers[i]:
        result.append(numbers[i])
        dp[i] = len(result)-1
    else:
        index = bisect_left(result,numbers[i])
        result[index] = numbers[i]
        dp[i] = index

max_len = len(result)-1
print(max_len)
idx = max_len
ans = []
for i in range(N,0,-1):
    if idx > 0 and idx == dp[i]:
        ans.append(numbers[i])
        idx -= 1

ans.reverse()
print(*ans)