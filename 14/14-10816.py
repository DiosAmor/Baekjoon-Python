N = int(input())
cards = list(map(int,input().split()))
M = int(input())
numbers = list(map(int,input().split()))

checked = [0]*(10000000*2+1)
for i in range(N):
    checked[cards[i]+10000000]+=1
for j in range(M):
    print(checked[numbers[j]+10000000],end=" ")