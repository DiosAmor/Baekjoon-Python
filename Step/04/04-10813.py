N,M=map(int,input().split())
numbers = list(range(1,N+1))
for _ in range(M):
    i,j=map(int,input().split())
    temp = numbers[i-1]
    numbers[i-1]=numbers[j-1]
    numbers[j-1]=temp
print(*numbers)