n = int(input())
p = 1000000007

matrix = [[1,1],[1,0]]
def mul(A,B):
    result = []
    for i in range(2):
        temp = []
        for j in range(2):
            temp2=0
            for k in range(2):
                temp2 += A[i][k]*B[k][j]
            temp.append(temp2 % p)
        result.append(temp)
    return result

def square(A,n):
    if n == 1:
        for i in range(2):
            for j in range(2):
                A[i][j] %= p
        return A
    temp = square(A,n//2)
    if n % 2 ==0:
        return mul(temp,temp)
    else:
        return mul(mul(temp,temp),A)

result = square(matrix,n)
print(result[0][1])