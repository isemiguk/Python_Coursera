from datetime import time

print(11 + 6)
print(11 - 6)
print(11 * 6)
print(11**6) #возведение в степень
print(11 / 6)
print(11 // 6) #целочисленное деление
print(11 % 6) #остаток от деления

#работа с переменными
speed = 100
time = 8
dist = speed * time
print(dist)

#удалить часть цифр с конца
n = int(input())
k = int(input())
print(n // 10 ** k)
