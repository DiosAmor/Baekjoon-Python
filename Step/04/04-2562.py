numbers=[]
for i in range(0,9):
    numbers.append(int(input()))
print(max(numbers))
print(numbers.index(max(numbers))+1)