n = int(input())

count = [1]*(n+1)
count[1] = 0
for i in range(4,n+1):
    temp = count[i-1] + 1
    if i%2 == 0:
        temp2 = count[int(i/2)] + 1
        temp = min(temp2,temp)
    if i%3 == 0:
        temp3 = count[int(i/3)] + 1
        temp = min(temp3,temp)
    count[i] = temp
print(count[n])
