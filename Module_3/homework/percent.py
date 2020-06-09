p = int(input())
x = int(input())
y = int(input())

amount = 100 * x + y
percentyear = amount * p // 100

total = amount + percentyear

print(total // 100, total % 100)
