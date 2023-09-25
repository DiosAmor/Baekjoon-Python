number = input()

numbers = [int(number[i]) for i in range(len(number))]
numbers.sort()
numbers.reverse()
print(*numbers,sep="")