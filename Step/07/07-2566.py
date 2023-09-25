N = []
N_max = []
N_max_index = []
for i in range(0,9):
    N_component = list(map(int,input().split()))
    N.append(N_component)
    N_max.append(max(N_component))
    N_max_index.append(N_component.index(max(N_component)))
N_max_total = max(N_max)
N_max_total_index = N_max.index(N_max_total)
print(N_max_total)
print("{} {}".format(N_max_total_index+1, N_max_index[N_max_total_index]+1))