X = int(input())

i=1
number = 1
while True:
    if X > number:
        i += 1
        number += i
    else:
        diff = number - X
        if i%2==0:
            print("{}/{}".format(i-diff,1+diff))
            break
        else:
            print("{}/{}".format(1+diff,i-diff))
            break