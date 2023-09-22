import sys
input = sys.stdin.readline

N, C = map(int,input().split())
x = [int(input()) for _ in range(N)]
x.sort()

start = 1
end = x[-1]-x[0]

while start<=end:
    mid = (start+end)//2
    cnt = 1
    check_x = x[0]
    for i in x:
        if i - check_x >= mid:
            cnt += 1
            check_x = i
    if cnt >= C:
        start = mid + 1
    else:
        end = mid - 1
print(end)
    