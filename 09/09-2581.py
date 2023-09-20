M = int(input())
N = int(input())

prime =[2]
for i in range(3,10000):
    check=0
    for j in range(0,len(prime)):
        if i % prime[j] == 0:
            check = 1
            break
    if check ==0:
        prime.append(i)

prime_numbers = []
for k in range(M,N+1):
    if prime.count(k) == 1:
        prime_numbers.append(k)
if len(prime_numbers) >0:
    print(sum(prime_numbers))
    print(prime_numbers[0])
else:
    print("-1")