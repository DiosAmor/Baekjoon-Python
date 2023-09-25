N,C = map(int,input().split())
w = list(map(int,input().split()))
w_a = w[:N//2]
w_b = w[N//2:]
w_a_total = []
w_b_total = []
cnt = 0

def cal_w_a_total(l,weight):
    if l >= len(w_a):
        w_a_total.append(weight)
        return
    cal_w_a_total(l+1,weight)
    cal_w_a_total(l+1,weight+w_a[l])

def cal_w_b_total(l,weight):
    if l >= len(w_b):
        w_b_total.append(weight)
        return
    cal_w_b_total(l+1,weight)
    cal_w_b_total(l+1,weight+w_b[l])

def lower_bound(start,end,key):
    while start < end:
        mid = (start+end)//2
        if w_b_total[mid] <= key:
            start = mid + 1
        else:
            end = mid
    return end

cal_w_a_total(0,0)
cal_w_b_total(0,0)
w_b_total.sort()

for i in w_a_total:
    if C - i >= 0:
        cnt+=(lower_bound(0,len(w_b_total),C-i))
print(cnt)