 # создание функций происходит с помощью команды def.
 # чтобы использовать как функцию, а не как процедуру, используется return
def hypot(a, b):
    sqrSum = a**2 + b**2
    return sqrSum**(1/2)

# определяют функцию до использования кода
print(hypot(3, 4))
