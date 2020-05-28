n = int(input())

textkorova = 'korova'
textkorovy = 'korovy'
textkorov = 'korov'

a = n % 10

if 10 < n < 20 or a == 0 or 5 <= a <= 9:
    print(n, textkorov, sep=' ')
elif a == 1:
    print(n, textkorova, sep=' ')
else:
    print(n, textkorovy, sep=' ')
