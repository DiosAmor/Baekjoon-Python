N = int(input())
# x_min, x_max
X = [10000, -10000]
# y_min, y_max
Y = [10000, -10000]

for _ in range(N):
    x, y = map(int,input().split())
    if X[0] > x:
        X[0] = x
    if X[1] < x:
        X[1] = x
    if Y[0] > y:
        Y[0] = y
    if Y[1] < y:
        Y[1] = y

print((Y[1]-Y[0])*(X[1]-X[0]))