N= int(input())

check = [False, False]+[True]*(N-1)

prime_num = []
for i in range(2,N+1):
    if check[i]:
        prime_num.append(i)
        for j in range(2*i,N+1,i):
            check[j] = False

left = 0
right = 0
total = 0
result = 0
while True:
    if right > len(prime_num):
        break
    else:
        if total > N:
            total -= prime_num[left]
            left += 1
        else:
            if total == N:
                result+=1
            if right < len(prime_num):
                total += prime_num[right]
            right += 1
            
print(result)
        