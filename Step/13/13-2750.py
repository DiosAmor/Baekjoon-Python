case = int(input())
numbers = [int(input()) for _ in range(case)]

for i in range(len(numbers)):
    for j in range(i):
        if numbers[i] < numbers[j]:
            temp = numbers[j:]
            temp.remove(numbers[i])
            numbers = numbers[:j] + [numbers[i]] + temp
            break
print(*numbers, sep="\n")