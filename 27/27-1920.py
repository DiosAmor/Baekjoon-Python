import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int,input().split()))
numbers.sort()

M = int(input())
targets = list(map(int,input().split()))

for i in targets:
    start = 0
    end = N-1
    mid = (end+start)//2
    check = 0
    while start <= end:
        mid = (end+start)//2
        if i > numbers[mid]:
            start = mid+1
        elif i < numbers[mid]:
            end = mid-1
        else:
            print(1)
            check = 1
            break
    if check == 0:
        print(0)