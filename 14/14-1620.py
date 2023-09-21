import sys
input = sys.stdin.readline

N, M = map(int,input().split())

dic = {}
for i in range(N):
    temp = input().strip()
    dic[temp] = i+1
    dic[str(i+1)] = temp
    
for _ in range(M):
    problem = input().strip()
    print(dic[problem])