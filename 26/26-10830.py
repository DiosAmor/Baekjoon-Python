import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
p = 1000

def mul(A,B):
    result = []
    for i in range(N):
        temp = []
        for j in range(N):
            temp2=0
            for k in range(N):
                temp2 += A[i][k]*B[k][j]
            temp.append(temp2 % p)
        result.append(temp)
    return result

def square(A,M):
    if M == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= p
        return A
    temp = square(A,M//2)
    if M % 2 ==0:
        return mul(temp,temp)
    else:
        return mul(mul(temp,temp),A)

result = square(A,M)
for i in range(N):
    print(*result[i])