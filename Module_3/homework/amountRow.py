n = int(input())

amount = 0

i = 1
while i <= n:
    amount = amount + (1 / i**2)
    i += 1

print('{0:.5f}'.format(amount))
