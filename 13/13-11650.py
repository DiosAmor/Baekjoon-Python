import sys

case = int(sys.stdin.readline())

coord = [list(map(int,sys.stdin.readline().split())) for _ in range(case)]
coord.sort()
for i in range(len(coord)):
    print("{} {}".format(coord[i][0], coord[i][1]))