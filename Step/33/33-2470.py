import sys
inf = sys.maxsize

N = int(input())

pH = list(map(int,input().split()))

pH.sort()
left = 0
right = N-1

answer = [left,right,abs(pH[left] + pH[right])]
while left < right:
    temp = pH[left] + pH[right]
    temp_abs = abs(temp)
    if temp_abs < answer[2]:
        answer = [left,right,temp_abs]
        if temp == 0:
            break
    if temp < 0:
        left += 1
    else:
        right -= 1
print(pH[answer[0]], pH[answer[1]])