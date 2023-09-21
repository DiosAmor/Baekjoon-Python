M, N = map(int,input().split())

sieve = [False, False] + [True]*(N-1)
prime = []

for i in range(2,N+1):
    if sieve[i]:
        prime.append(i)
        for j in range(2*i,N+1,i):
            sieve[j] = False
            
for k in range(len(prime)):
    if prime[k] >= M:
        print(prime[k])