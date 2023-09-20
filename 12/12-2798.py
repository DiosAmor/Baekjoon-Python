import itertools

N,M = map(int, input().split())
numbers = list(map(int,input().split()))

poss = list(itertools.combinations(numbers,3))
max_value = 0
for i in poss:
    if max_value < sum(i) and sum(i)<=M:
        max_value = sum(i)
print(max_value)

