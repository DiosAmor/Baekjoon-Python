#pypy

N, M = map(int,input().split())
woods = list(map(int,input().split()))

woods.sort()
start = 1
end = max(woods)

while start <= end:
    mid = (start+end)//2
    temp = 0
    for i in woods:
        diff = i - mid
        if diff > 0:
            temp += diff
    if temp >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)