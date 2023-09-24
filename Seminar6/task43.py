# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

# мой вариант
# num_list = [int(input(f"{i+1}: ")) for i in range(int(input('Введите длину списка: ')))]
# num_count = 0
# for i in range(len(num_list)):
#     num_count+= num_list.count(i)//2
# print(num_count)


# вариант через разницу в кол-ве элементов списка и множества
list_1 = [int(input()) for i in range(int(input()))]
set_1 = list(set(list_1))
print(sum(list_1.count(set_1[i])//2 for i in range(len(set_1))))