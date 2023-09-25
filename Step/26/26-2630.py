N = int(input())

paper = [list(map(int,input().split())) for _ in range(N)]

cnt_w = 0
cnt_b = 0
def div_paper(x,y,N):
    global cnt_w, cnt_b
    check = 0
    for i in range(x,x+N):
        for j in range(y,y+N):
            if paper[i][j]:
                check += 1
    if check == 0:
        cnt_w += 1
    elif check == N**2:
        cnt_b += 1
    else:
        div_paper(x,y,N//2)
        div_paper(x+N//2,y,N//2)
        div_paper(x,y+N//2,N//2)
        div_paper(x+N//2,y+N//2,N//2)
div_paper(0,0,N)
print(cnt_w)
print(cnt_b)