while True:
    Sen = input()
    if Sen == '.':
        break
    stack = []
    check = 0
    for i in range(len(Sen)):
        if Sen[i] == '(':
            stack.append(0)
        if Sen[i] == '[':
            stack.append(1)
        if Sen[i] == ')':
            if len(stack) > 0 and stack[len(stack)-1] == 0:
                stack.pop()
            else:
                print("no")
                check = 1
                break
        if Sen[i] == ']':
            if len(stack) > 0 and stack[len(stack)-1] == 1:
                stack.pop()
            else:
                print("no")
                check = 1
                break
    if len(stack) == 0 and check == 0:
        print("yes")
    if len(stack) > 0 and check == 0:
        print("no")