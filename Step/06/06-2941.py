words = '!'+input()+'!!'

word_count=0
for i in range(1,len(words)-2):
    if words[i] == 'c':
        if words[i+1] == '=' or words[i+1] == '-':
            pass
        else:
            word_count+=1
    elif words[i] == 'd':
        if words[i+1] == 'z' and words[i+2] =='=':
            pass
        elif words[i+1] == '-':
            pass
        else:
            word_count+=1
    elif words[i] == 'l' and words[i+1] =='j':
        pass
    elif words[i] == 'n' and words[i+1] =='j':
        pass
    elif words[i] == 's' and words[i+1] =='=':
        pass
    elif words[i] == 'z' and words[i+1] =='=':
        pass
    else:
        word_count+=1
print(word_count)