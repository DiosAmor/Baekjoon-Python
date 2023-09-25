n = int(input())

total = [0]
for _ in range(n):
    numbers = list(map(int,input().split()))
    temp = []
    if _ == 0:
        temp.append(numbers[0])
    elif _ == 1:
        temp = [numbers[0]+total[0], numbers[1]+total[0]]
    else:
        for i in range(len(numbers)):
            if i == 0:
                temp.append(total[0]+numbers[0])
            elif i == len(numbers)-1:
                temp.append(total[-1]+numbers[-1])
            else:
                temp.append(max(total[i-1],total[i])+numbers[i])
    total = temp
print(max(total))            