str = input()

letterFstart = str.find('f')
letterFend = str.rfind('f')

if letterFstart != -1:
    if letterFstart == letterFend:
        print(letterFstart)
    else:
        print(letterFstart, letterFend, sep=' ')
