#A~Z 10~35
#ord(A) = 65
#A = chr(10+55)

N,B = map(int,input().split())
result = []
while N>=B:
    temp = N%B
    if temp >9:
        temp = chr(temp+55)
    result.append(str(temp))
    N = N//B

if N>9:
    N = chr(N+55)
result.append(str(N))
result.reverse()
print("".join(result))
