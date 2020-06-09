n = float(input())

number = int(n)
fraction = int((n - int(n)) * 10)

if fraction >= 5:
    number += 1

print(number)
