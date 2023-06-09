# list_1 = []
# list_1 = list()
# print(list_1)
# list_1 = [1, 2, 3, 4, 5]
# print(list_1)
# print(*list_1)

# print(len(list_1))

# print(list_1[0])

# print(list_1[-1]) #последнее с конца

# list_2 = [1,5]
# print(*list_2)
# list_2.append(8)
# print(*list_2)
# list_2.append(99)
# print(*list_2)

# list_3 = []
# for i in range(5):
#     list_3.append(i*i)
#     print(list_3)

# list_1 = [1, 2, 3, 4, 5]
# list_1.pop()
# print(list_1)
# list_1.pop()
# print(list_1)
# list_1.pop()
# print(list_1)
# удаляет элемент и возвращает его:

# list_1 = [1, 2, 3, 4, 5]
# a = list_1.pop()
# b = list_1.pop()
# c = list_1.pop()
# print(a, b, c)

# list_1 = [1, 2, 3, 4, 5]
# list_1.insert(2,10)
# print(list_1)

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) #[9, 10]
# print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6]) # [1, 7]
# print(list_1[::6]) # [1, 7]

# Кортежи

# t = ()

# print(type(t))

# t = (1, )
# print(type(t))

# v = [1, 2, 3]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))

# a, b, c = v

# print(a, b, c)

# t = (1, 2, 3, 4, 5,)

# for i in t:
#     print(i)

# for i in range(len(t)):
#     print(t[i])

# t = () # создание пустого кортежа
# print(type(t)) # class <'tuple'>
# t = (1,)
# print(type(t))
# t = (1)
# print(type(t))
# t = (28, 9, 1990)
# print(type(t))
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')
# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# for e in t:
#     print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support(нельзя изменять кортеж)

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue

# t[0] = 2 #выдает ошибку


# d = {}
# d = dict()

# d['q'] = 'qwerty'
# print(d)
# print(d['q'])

# d['w'] = 'wasdf'
# print(d)
# print(d['w'])

# dictionary = {}
# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться
# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →


# colors = {'red', 'green', 'blue'}
# print(colors)  # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors)  # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors)  # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors)  # {'green', 'blue','gray'}
# colors.remove('red')  # KeyError: 'red'
# colors.discard('red')  # удаляет, если уже отсутствует то кайф и не выдает ошибку
# print(colors)  # {'green', 'blue','gray'}
# colors.clear()  # { }
# print(colors)  # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

a = {1, 2, 3, 4, 7}
b = {3, 4, 2, 5, 6}

c = a.copy()

print(a,b,c)
e = a.union(b)
print(e)
i = a.intersection(b)
print(i)
dif = a.difference(b)
print(dif)

q = a.union(b).difference(a.intersection(b))