H,M=map(int,input().split())
duration = int(input())
time=H*60+M
time_edit = time+duration
if time_edit >= 24*60:
    time_edit -= 24*60
H_edit = time_edit//60
M_edit = time_edit%60

print("{0} {1}".format(H_edit,M_edit))