my_list = [1, 2, 3, 3]  # список использует квадратные скобки
b = my_list  # т.к. список изменяемый, и пайтон хранит ссылки, то изменяя b, изменится и my_list
c = my_list[:]  # пример реализации копии спискаб создасться новй объект в памяти для c
print(c)
print(*c)  # пример вывода списка как цифры

print(list('abcde'))  # получение списка по буквенно из строки

print('red,green,  blue'.split(sep=','))  # получение списка из строки, разделенных разделителем. Если не указан sep, то используется пробел табуляция перевод строки

print(list(map(len, ['red', 'green', 'blue'])))  # MAP позволяет применить каждому объекту итерации, какую-то функцию. Первый параметр это функция, а второй - iterable элементов, к которому нужно применить эту функцию

# numList = list(map(int, input().split()))  # пример получения списка цифр 
# print(numList)

print(', '.join(['Veni', 'Vidi', 'Vici']))  # объединение в строки с указанием разделителя

# Методы, не изменяющие список и возвращающие значение:

# count(x) - подсчитывает число вхождений значения x в список. Работает за время O(N)
# index(x) - находит позицию первого вхождения значения x в список. Работает за время O(N)
# index(x, from) - находит позицию первого вхождения значения x в список, начиная с позиции from. Работает за время O(N)

# Методы, не возвращающие значение, но изменяющие список:

# append(x) - добавляет значение x в конец списка
# extend(otherList) - добавляет все содержимое списка otherList в конец списка. В отличие от операции + изменяет объект к которому применен, а не создает новый
# remove(x) - удаляет первое вхождение числа x в список. Работает за время O(N)
# insert(index, x) - вставляет число x в список так, что оно оказывается на позиции index. Число, стоявшее на позиции index и все числа правее него сдвигаются на один вправо. Работает за время O(N)
# reverse() - Разворачивает список (меняет значение по ссылке, а не создает новый список как myList[::-1]). Работает за время O(N)

# Методы, возвращающие значение и изменяющие список:

# pop() - возвращает последний элемент списка и удаляет его
# pop(index) - возвращает элемент списка на позиции index и удаляет его. Работает за время O(N)


# пример удаления нечетных чисел
# работает неправильно, т.к. индексы при удалении смещаются
numbers = list(map(int, input().split()))
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        numbers.pop(i)
print(' '.join(map(str, numbers)))

# пример удаления нечетных чисел через while. Метод POP нерекомендуемый
numbers = list(map(int, input().split()))
i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        numbers.pop(i)
    else:
        i += 1
print(' '.join(map(str, numbers)))

# рекомендуемый пример удаления из списка. Создавая и заполняя второй список, не удаляя данне из первого
numbers = list(map(int, input().split()))
newList = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        newList.append(numbers[i])
print(' '.join(map(str, newList)))