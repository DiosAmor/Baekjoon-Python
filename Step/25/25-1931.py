import sys
input = sys.stdin.readline

N = int(input())
meet = [list(map(int,input().split())) for _ in range(N)]

meet.sort(key=lambda x:x[0])
meet.sort(key=lambda x:x[1])

count = 1
end = meet[0][1]
for i in range(1,N):
    if meet[i][0] >= end:
        count +=1
        end = meet[i][1]
print(count)