#A~Z 10~35
#ord(A) = 65
#A = ord(A)-55

N,B = input().split()
B = int(B)
length = len(N)
result = 0
for i in range(length):
    if N[i].isdigit():
        result += int(N[i])*B**(length-1-i)
    else:
        result += (ord(N[i])-55)*B**(length-1-i)
print(result)