while(1):
    try:
        sen = input()
        print(sen)
    except EOFError:
        break