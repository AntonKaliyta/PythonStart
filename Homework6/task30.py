# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


num_list = []
num_list.append(int(input('Введите первый элемент: ')))
length = int(input('Введите длину списка: '))
difference = int(input('Введите разность элементов: '))
for i in range(2, length+1):
    num_list.append(num_list[0] + (i-1) * difference)
print(num_list)



# a1 = int(input())
# d = int(input())
# n = int(input())
# for i in range(n):
#     print(a1 + i * d, end=' ')
