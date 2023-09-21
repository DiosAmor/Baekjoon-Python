case = int(input())

for _ in range(case):
    check_stack = []
    stack_check = 0
    Test = input()
    for i in range(len(Test)):
        if Test[i] == '(':
            check_stack.append(1)
        else:
            if len(check_stack) > 0:
                check_stack.pop()
            else:
                print("NO")
                stack_check = 1
                break
    if len(check_stack) == 0 and stack_check == 0:
        print("YES")
    if len(check_stack) > 0 and stack_check == 0:
        print("NO")