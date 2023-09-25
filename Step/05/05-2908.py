a,b = input().split()
a_edit = int(a[2]+a[1]+a[0])
b_edit = int(b[2]+b[1]+b[0])
if a_edit > b_edit:
    print(a_edit)
else:
    print(b_edit)