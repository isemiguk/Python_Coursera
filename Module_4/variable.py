def f():
    a = 1  # локальная переменная, используется только в функции
    print(a)

a = 0  # глобальная переменная, доступна в том числе и в функции (можно не передавать как параметр)
f()

print(a)


# изменение глобальной переменной внутри функции
def f1():
    global a
    print(a)   
    a = 1  # изменение глобальной переменной
   
a = 0  # глобальная переменная, доступна в том числе и в функции (можно не передавать как параметр)
f1()

print(a)