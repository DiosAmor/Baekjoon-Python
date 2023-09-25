N, X = map(int,input().split())
test = list(map(int,input().split()))

for i in range(0,len(test)):
    if X > test[i]:
        print(test[i],end=" ")
