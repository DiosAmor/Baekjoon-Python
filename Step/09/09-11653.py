number = int(input())

for k in range(2,number+1):
    if number == 1:
        break
    while True:
        if number % k ==0:
            number = number // k
            print(k)
        else:
            break
    