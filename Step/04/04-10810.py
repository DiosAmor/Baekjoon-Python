N,M=map(int,input().split())
numbers = [0]*N
for m in range(M):
    i,j,k = map(int,input().split())
    for c in range(i,j+1):
        numbers[c-1] = k

print(*numbers)