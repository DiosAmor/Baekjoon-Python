N,K = map(int,input().split())

p = 1000000007

def fac(n1,n2):
    temp = 1
    for i in range(n1,n2+1):
        temp = (temp*i) % p
    return temp

def square(a,b):
    if b == 1:
        return a%p
    temp = square(a,b//2)
    if b%2==0:
        return temp*temp%p
    else:
        return temp*temp*a%p
    
print(fac(N-K+1,N)*square(fac(2,K),p-2)%p)