N = int(input())

max_num_5 = N//5+1
max_num_3 = N//3+1
num = -1
for i in range(max_num_5,-1,-1):
    weight_5 = 5*i
    num_3 = (N-weight_5)//3
    if num_3 < 0:
        num_3 = 0
    if (weight_5+num_3*3 == N):
        num = i+num_3
        break
for j in range(1,max_num_3):
    weight_3 = 3*j
    num_5 = (N-weight_3)//5
    if num_5 < 0:
        num_5 = 0
    if (weight_3+num_5*5 == N):
        if num ==-1:
            num = j+num_5
            break
        elif num !=-1 and num>j+num_5:
            num = j+num_5
            break
print(num)