import sys

N,M = map(int,sys.stdin.readline().split())
A = [sys.stdin.readline().strip() for _ in range(N)]
B = [sys.stdin.readline().strip() for _ in range(M)]
A = set(A)
B = set(B)

C = A&B
print(len(C))
C = list(C)
C.sort()
print(*C,sep="\n")