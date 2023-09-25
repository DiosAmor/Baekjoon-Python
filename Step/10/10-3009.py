x = []
y = []
for _ in range(3):
    temp_x,temp_y = map(int,input().split())
    x.append(temp_x)
    y.append(temp_y)
    
result_x, result_y = 0, 0
for i in range(3):
    if x.count(x[i]) == 1:
        result_x = x[i]
    if y.count(y[i]) == 1:
        result_y = y[i]
        
print(result_x,result_y)
        