str = input()

posF = str.find('f')
if posF != -1:
    fragment = str[posF + 1:]
    twoposF = fragment.find('f')
    if twoposF != -1:
        print(posF + twoposF + 1)
    else:
        print(-1)
else:
    print(-2)
