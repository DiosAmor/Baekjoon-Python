import sys
N,S = map(int,input().split())

numbers = list(map(int,input().split()))
left = 0
right = 0
total = 0
min_len = sys.maxsize

while True:
    if total >= S:
        min_len = min(min_len,right-left)
        total -= numbers[left]
        left += 1
    elif right > N-1:
        break
    else:
        total += numbers[right]
        right += 1
        
if min_len == sys.maxsize:
    print(0)
else:
    print(min_len)
