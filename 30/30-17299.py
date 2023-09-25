from collections import Counter

N = int(input())
numbers = list(map(int,input().split()))
results = [-1] * N

numbers_edit = Counter(numbers)
stack = []


stack.append(0)
for i in range(1, N):
    while stack and numbers_edit[numbers[stack[-1]]] < numbers_edit[numbers[i]]:
        results[stack.pop()] = numbers[i]
    stack.append(i)


print(*results)