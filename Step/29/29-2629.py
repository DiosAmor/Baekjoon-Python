N = int(input())
weight = list(map(int,input().split()))
M = int(input())
ball = list(map(int,input().split()))
result = []
weight = [0] + weight

dp = [[0]*15001 for _ in range(31)]
def check(idx,w):
    global N
    if dp[idx][w] == 1:
        return
    dp[idx][w] = 1
    if idx < N:
        check(idx+1,w)
        check(idx+1,w+weight[idx+1])
        check(idx+1,abs(w-weight[idx+1]))

check(0,0)
result = []
for i in range(M):
    if ball[i] <= 15000 and dp[N][ball[i]] == 1:
        result.append("Y")
    else:
        result.append("N")
print(*result,sep=" ")