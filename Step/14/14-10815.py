N = int(input())
cards = list(map(int,input().split()))
M = int(input())
numbers = list(map(int,input().split()))
max_num = 10000000
checked = [0]*(max_num*2+1)
for i in range(N):
    checked[cards[i]+max_num]=1
for j in range(M):
    print(checked[numbers[j]+max_num],end=" ")