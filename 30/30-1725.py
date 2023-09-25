import sys
input = sys.stdin.readline     
N = int(input())
rect = [0]+[int(input()) for _ in range(N)]
stack = [[0,0]]
rect.append(0)
max_size = 0
for i in range(1,N+2):
    while stack[-1][0] > rect[i]:
        height, index = stack.pop()
        while stack[-1][0] == height:
            stack.pop()
        size = max(height * (i-1-stack[-1][1]), height * (i-index))
        if max_size < size:
            max_size = size
        if len(stack) == 0:
            break
    stack.append([rect[i],i])
print(max_size)