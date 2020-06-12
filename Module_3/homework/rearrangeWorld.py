str = input()

posSpace = str.find(' ')
print(str[posSpace + 1:], str[:posSpace], sep=' ')
