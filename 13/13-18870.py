import sys
n= sys.stdin.readline()
coord = list(map(int,sys.stdin.readline().split()))
coord_edit = set(coord)
coord_edit = sorted(list(coord_edit))
for i in coord:
    start =0
    end = len(coord_edit)-1
    while start <= end:
        mid = (start+end)//2
        if coord_edit[mid]==i:
            print(mid,end=" ")
            break
        elif coord_edit[mid]<i:
            start=mid+1
        else:
            end=mid-1
