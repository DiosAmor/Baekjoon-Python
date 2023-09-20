N = int(input())
number = 1
i=1
while True:
    if number >= N:
        print(i)
        break
    else:
        number += 6*i
        i+=1