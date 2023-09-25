import sys

case = int(sys.stdin.readline())
numbers =[]
for _ in range(case):
    temp = list(map(int,sys.stdin.readline().split()))
    temp.reverse()
    numbers.append(temp)
numbers.sort()
for i in range(case):
    print("{} {}".format(numbers[i][1], numbers[i][0]))