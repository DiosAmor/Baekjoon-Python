N,M = map(int,input().split())
numbers = list(range(1,N+1))

for _ in range(M):
    i,j=map(int,input().split())
    numbers = numbers[:i-1]+list(reversed(numbers[i-1:j]))+numbers[j:]
print(*numbers)