myTuple = (1, 2, 3)  # tuple = кортеж. Хранит что-то неизменяемое. Для изменяемых используется список
print(myTuple[1])

sTuple = (4, 5, 6)
print(myTuple + sTuple)  # сложение (склеивание кортежей). Многие методы работают как и у строки

print(len(sTuple))

bTuple = (1, 'fb', 3.14)  # можно хранить разные типы
print(bTuple)

singleTone = (7,)  # singleTone - кортеж из 1-го элемента
print(singleTone)
number = (7)  # а так просто число (без указания запятой)
print(number)

cTuple = (1, (2, 3), (4,))  # пример вложенных кортежей
print(cTuple)
print(cTuple[1][0])

man = ('Ivan', 'Ivanov', 28)
print(man[-1])  # по аналогии со строками обращаемся к элементам с конца

dTuple = 1, 'fb', 3.14  # пример записи кортежа
a, b, c = dTuple
print(b)

print((1, 2) + (3, 4))  # в этом случае, результат без скобок и со скобками будет различен
print(1, 2 + 3, 4)  # в этом случае, результат без скобок и со скобками будет различен

name_and_age = ('Bob', 42)
(name, age) = name_and_age
print(name)  # 'Bob'
print(age)   # 42

a = 1
b = 2
a, b = b, a  # изменение мест переменных
print(a, b)  