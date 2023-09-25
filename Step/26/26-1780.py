N = int(input())

paper = [list(map(int,input().split())) for _ in range(N)]

cnt_minus = 0
cnt_zero = 0
cnt_plus = 0

def div_paper(x,y,N):
    global cnt_minus, cnt_zero, cnt_plus
    check_count = 0
    check = paper[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if paper[i][j] == check:
                check_count += 1
    if check_count == N**2:
        if check == 1:
            cnt_plus += 1
        elif check == 0:
            cnt_zero += 1
        else:
            cnt_minus += 1
    else:
        for i in range(3):
            for j in range(3):
                div_paper(x+i*N//3,y+j*N//3,N//3)
div_paper(0,0,N)
print(cnt_minus)
print(cnt_zero)
print(cnt_plus)