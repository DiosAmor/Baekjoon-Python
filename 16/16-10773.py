import sys
input = sys.stdin.readline

K = int(input())
numbers = []
for _ in range(K):
    N = int(input())
    if N == 0:
        numbers.pop()
    else:
        numbers.append(N)
print(sum(numbers))