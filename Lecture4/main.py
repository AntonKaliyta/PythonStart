# def f(x):
#     return x*x

# a = f
# print(a(5))
# print(f(5))


# def calk1(a, b):
#     return a + b

# def calk2(a,b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# math(calk1, 5, 10)
# math(calk2, 5, 10)


# Lambda аргументы: выражение
# double = lambda x: x*4
# print(double(5))
# 20
# таким образом double = lambda x: x*2   == def double(x):
# return x * 2


# def defined_cube(y):
#     return y*y*y

# lambda_cube = lambda y: y*y*y
# print(defined_cube(2))
# print(lambda_cube(2))

# Без использования лямбды: Здесь обе функции возвращают заданное значение, возведенное в куб. Но при использовании def,
# нам пришлось определить функцию с именем и defined_cube() дать ей входную величину.
# После выполнения нам также понадобилось возвратить результат, из того места, откуда была вызвана функция, и мы сделали это,
# используя ключевое слово return.

# С применением лямбды: Определение лямбды не включает оператор return, а всегда содержит возвращенное выражение.
# Мы также можем поместить определение лямбды в любое место, где ожидается функция, и нам не нужно присваивать его переменной.
# Так выглядят простые лямбда-функции.


# Функция filter() в Python принимает в качестве аргументов функцию и список .
# Функция вызывается со всеми элементами в списке, и в результате возвращается новый список, содержащий элементы,
# для которых функция результирует в True.
# Вот пример использования функции filter() для отбора четных чисел из списка.

# my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
# new_list_even = list(filter(lambda x: (x%2 == 0) , my_list))
# new_list_odd = list(filter(lambda x: (x%2!= 0) , my_list))
# print(new_list_even)
# print(new_list_odd)

# my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
# new_list = list(filter(lambda x: x >10, my_list))
# print(new_list)


# Функция map() принимает в качестве аргументов функцию и список.
# Функция вызывается со всеми элементами в списке, и в результате возвращается новый список, содержащий элементы,
# возвращенные данной функцией для каждого исходного элемента.
# Ниже пример использования функции map() для удвоения всех элементов списка.

# current_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
# new_list = list(map(lambda x: x*2 , current_list))
# print(new_list)


# В этом примере мы будем использовать лямбда-функцию со списковым включением и лямбда-функцию с циклом for.
# Мы выведем на экран  таблицу из 10 элементов.

# tables = [lambda x = x: x*10 for x in range(1, 11)]
# for i in tables:
#     print(i(), end=' ')

# new_list = [lambda x = x: x*5 for x in range(1,6)]
# for i in new_list:
#     print(i())


# задача
# my_list = [1, 2, 3, 5, 6, 15, 23, 38]
# new_list = []
# for i in my_list:
#     if i%2 ==0:
#         new_list.append((i, i**2))
# print(new_list)


# list_1 = [i for i in range (1,10)]
# list_1 = list(map(lambda x: x*10, list_1))
# print(list_1)

# data = '234 23 21 35'
# print(data)
# data = list(map(int, data.split()))
# print(data)

# list_1 = [2, 4, 5, 6, 7]
# new_list = list(filter(lambda x: x%2 == 0, list_1))
# print(new_list)


# s = 'abc'
# t = (10, 20, 30)
# print(list(zip(s,t)))




# colors = ['red', 'greeb', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.close


# with open('file.txt', 'a') as data:
#     data.write('\n')
#     data.write('line 1\n')
#     data.write('line 2\n')

# path = 'file.txt'
# data = open('file.txt', 'r')
# for i in data:
#     print(i)
# data.close()


# import os

# print(os.getcwd())