N = int(input())
numbers = list(map(int,input().split()))
results = [-1] * N
stack = []


stack.append(0)
for i in range(1, N):
    while stack and numbers[stack[-1]] < numbers[i]:
        results[stack.pop()] = numbers[i]
    stack.append(i)


print(*results)