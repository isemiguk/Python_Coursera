number = int(input())

n1 = '+___ '
n2 = '|1 / '
n3 = '|__\ '
n4 = '|    '

print(n1 * number)

n21 = ''
i = 1
while i <= number:
    n21 += n2.replace('1', str(i))
    i += 1
print(n21)
print(n3 * number)
print(n4 * number)
