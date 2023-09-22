n = int(input())
pos = []
dp = [1]*n
for _ in range(n):
    temp = list(map(int,input().split()))
    pos.append(temp)

pos.sort(key=lambda x: x[0])

for i in range(n):
    for j in range(i):
        if pos[i][1] > pos[j][1]:
            dp[i] = max(dp[i],dp[j]+1)
print(n-max(dp))
