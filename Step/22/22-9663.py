#pypy

num = int(input())

count = 0
chess = []

def check(n):
    for i in range(n):
        if (chess[n] == chess[i]) or (abs(chess[n] - chess[i])  == n-i):
            return False
    return True

def queen(n):
    global count
    if n==num:
        count += 1
        return
    for i in range(num):
        chess.append(i)
        if check(n):
            queen(n+1)
        chess.pop()

queen(0)
print(count)