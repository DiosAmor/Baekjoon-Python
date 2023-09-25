number = int(input())
scores = list(map(int,input().split()))
average = sum(scores)/number*100/max(scores)
print(average)