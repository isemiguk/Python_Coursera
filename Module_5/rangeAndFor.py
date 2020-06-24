myRange = range(10)  # объект iterable (к элементам которых можно получать последовательный доступ), состоящие из целых чисел.
print(tuple(myRange))

fio = 'Ivanov Ivan Ivanovich'
fioTuple = tuple(fio)  # каждую букву строки возьмет в элемент кортежа
print(fioTuple)

for color in ('red', 'green', 'yellow'):
    print('apple ', color)

for i in range(5):
    print(i)

for i in range(10, 15):
    print(i)

for i in range(10, 15, 3):  # 1 параметр - от, 2 - до, 3 - шаг
    print(i)

for i in range(3, -1, -1):  # обратный порядок
    print(i, end=' ')
print()

for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end=' ')
    print()
