import math
A,B,V = map(int,input().split())

height = V-A
days=math.ceil(height/(A-B))
print(days+1)