N, M = map(int,input().split())

num = list(map(int,input().split()))

dp = [0]*M
dp[0] = 1
total = 0

for i in range(N):
    total += num[i]
    r = total % M
    dp[r] += 1

count = 0
for i in dp:
    count += i*(i-1)//2
    
print(count)