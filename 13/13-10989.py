import sys
input = sys.stdin.readline

cnt = [0]*10001
N = int(input())

for _ in range(N):
    cnt[int(input())] += 1

for i in range(10001):
    if cnt[i] != 0:
        for j in range(cnt[i]):
            print(i)