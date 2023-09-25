N = int(input())

numbers = list(map(int,input().split()))

numbers.sort()

X = int(input())

left = 0
right = N-1
result = 0

while left < right:
    temp = numbers[left] + numbers[right]
    if X == temp:
        result += 1
        right -= 1
    elif X > temp:
        left += 1
    else:
        right -= 1
print(result)