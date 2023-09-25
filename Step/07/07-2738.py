N,M = map(int,input().split())
A = []
for i in range(0,N):
    A_com = list(map(int,input().split()))
    A.append(A_com)
B = []
for j in range(0,N):
    B_com = list(map(int,input().split()))
    B.append(B_com)
for k in range(0,N):
    for l in range(0,M):
        print(A[k][l]+B[k][l],end=" ")
    print()
