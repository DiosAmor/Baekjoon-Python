n = 123456*2
s = [False,False]+[True]*(n-1)
prime = []

for i in range(2,n+1):
    if s[i] == True:
        prime.append(i)
        for j in range(2*i,n+1,i):
            s[j] = False

while True:
    a = int(input())
    if a == 0:
        break
    else:
        number = 0
        for k in prime:
            if k > a and k <= 2*a:
                number += 1
            if k > 2*a:
                break
        print(number)