import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
M,K = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(M)]

for i in range(N):
    temp = []
    for j in range(K):
        temp2=0
        for k in range(M):
            temp2 += A[i][k]*B[k][j]
        temp.append(temp2)
    print(*temp,sep=" ")
