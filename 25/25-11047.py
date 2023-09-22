import sys
input = sys.stdin.readline

N,K = map(int,input().split())
coins = [int(input()) for _ in range(N)]

coins.reverse()
count = 0
for i in range(N):
    count += K // coins[i]
    K = K % coins[i]

print(count)