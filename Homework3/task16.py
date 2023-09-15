# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# arrayA = []
# n = int(input('Введите кол-во элементов в массиве: '))

# arrayA = [i for i in range(1, n+1)]
# print(arrayA)

# x = int(input('Введите искомое число: '))

# count = 0
# for i in range(len(arrayA)):
#     if i == x:
#         count += 1  
# print(count)



from random import choices 

num = int(input('Введите кол-во элементов в массиве: '))
arrayA = choices(range(num * 2), k = num)
print(arrayA)

result = arrayA.count(int(input('Введите искомое число: ')))
print(result)


