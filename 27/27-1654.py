import sys
input = sys.stdin.readline

N, K = map(int,input().split())
lan = [int(input()) for _ in range(N)]

start = 1
end = max(lan)

while start <= end:
    mid = (start+end)//2
    temp = 0
    for i in lan:
        temp += i//mid
    if temp >= K:
        start = mid + 1
    else:
        end = mid - 1
print(end)