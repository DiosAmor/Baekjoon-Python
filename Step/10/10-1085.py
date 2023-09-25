x,y,w,h = map(int,input().split())

if x<=w//2:
    diff_x = x
else:
    diff_x = w-x
if y<=h//2:
    diff_y = y
else:
    diff_y = h-y


diff = min([diff_x,diff_y])

print(diff)