number = int(input())
case = list(map(int,input().split()))

prime = [2]
for i in range(3,1000):
    check = 0
    for j in range(len(prime)):
        if i % prime[j] == 0:
            check = 1
            break
    if check != 1:
        prime.append(i)

prime_case = 0
for k in case:
    if prime.count(k) == 1:
        prime_case += 1
print(prime_case)
            