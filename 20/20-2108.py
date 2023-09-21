import sys

n = int(sys.stdin.readline())
num_list = [0] * 8001

for _ in range(n):
    num_list[int(sys.stdin.readline())+4000] += 1

sort_num = []
for i in range(8001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            sort_num.append(i-4000)

print(round(sum(sort_num)/n))
print(sort_num[len(sort_num)//2])

frequency = max(num_list)
if num_list.count(frequency)>1:
    num_list[num_list.index(frequency)]=0
print(num_list.index(frequency)-4000)
print(sort_num[len(sort_num)-1]-sort_num[0])