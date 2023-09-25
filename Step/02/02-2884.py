H,M=map(int,input().split())
time=H*60+M
time_edit = time-45
if time_edit < 0:
    time_edit += 24*60
H_edit = time_edit//60
M_edit = time_edit%60

print("{0} {1}".format(H_edit,M_edit))
