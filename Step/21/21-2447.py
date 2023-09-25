num = int(input())
stars=[[True]*num for _ in range(num)]

def star_del(x,y,n):
    if n==1:
        return stars
    else:
        for i in range(n//3):
            for j in range(n//3):
                stars[x+n//3+i][y+n//3+j]=False
        for i in range(3):
            for j in range(3):
                star_del(x+i*n//3,y+j*n//3,n//3)
        return stars
star_del(0,0,num)

for i in range(num):
    for j in range(num):
        if stars[i][j] == True:
            print("*",end='')
        else:
            print(" ",end='')
    print()