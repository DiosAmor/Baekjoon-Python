N,K = map(int,input().split())

def fac(num,result):
    if num == 0:
        return result
    return fac(num-1,result*num)

temp = fac(N,1)/(fac(K,1)*fac(N-K,1))
print(int(temp))