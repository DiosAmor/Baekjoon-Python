import sys
input = sys.stdin.readline

N = int(input())
height = [int(input()) for _ in range(N)]
stack = []
result = 0
for i in range(0,N):
    while stack and stack[-1][0] < height[i]:
        result+=stack.pop()[1]
    if stack and stack[-1][0] == height[i]:
        temp = stack.pop()[1]
        result+=temp
        if stack:
            result+=1
        stack.append((height[i],temp+1))
    else:
        if stack:
            result+=1
        stack.append((height[i],1))
print(result)