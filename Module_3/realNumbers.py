print(float(2**100)) #пример преобразования в вещественное число

if 0.1 + 0.2 == 0.3: #это связано с представлением вещественных чисел в пайтоне
    print('yes')
else:
    print('no')


print('{0:.25f}'.format(0.1)) #пример указания вывода количества знаков после запятой
print(0.5.as_integer_ratio()) #пример хранения в виде дроби  (числитель и знаменатель)

# пример сравнения вещественных чисел
x = float(input())
y = float(input())
epsilon = 10 ** -6
if abs(x - y) < epsilon:
    print('yes')
else:
    print('yes')