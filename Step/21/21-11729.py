num = int(input())

record =[]
def hanoi(n,from_pos,to_pos,aux_pos):
    if n ==1:
        record.append([from_pos,to_pos])
        return
    # 1번 과정
    hanoi(n-1,from_pos,aux_pos,to_pos)
    # 2번 과정
    record.append([from_pos,to_pos])
    # 3번 과정
    hanoi(n-1,aux_pos,to_pos,from_pos)

hanoi(num,1,3,2)

print(len(record))
for i in record:
    print("{} {}".format(i[0],i[1]))