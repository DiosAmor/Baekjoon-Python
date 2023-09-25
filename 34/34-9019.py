#pypy

from collections import deque
import sys
input = sys.stdin.readline
max_num = 10000


T = int(input())
for _ in range(T):
    A, B = map(int,input().split())
    layer = deque([[A,""]])
    visit = [0]*max_num
    visit[A] = 1
    while layer:
        num,order = layer.popleft()
        if num == B:
            print(order)
            break
        #D
        num_new = (2*num) % max_num
        if not visit[num_new]:
            layer.append([num_new,order+"D"])
            visit[num_new] = 1
        #S
        num_new = (num-1) % max_num
        if not visit[num_new]:
            layer.append([num_new,order+"S"])
            visit[num_new] = 1
        #L
        num_new = (10*num+num//1000) % max_num
        if not visit[num_new]:
            layer.append([num_new,order+"L"])
            visit[num_new] = 1
        #R
        num_new = (num//10+(num%10)*1000) % max_num
        if not visit[num_new]:
            layer.append([num_new,order+"R"])
            visit[num_new] = 1