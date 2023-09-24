# n = int(input('Введите кол-во элементов первого массива: '))
# first = [int(input(i)) for i in range(n)]
# # print(first)
# m = int(input('Введите кол-во элементов второго массива: '))
# second = [int(input(i)) for i in range (m)]
# # print(second)

# first,second = set(first), set(second)
# print(first.difference(second))




# Вариант интерфейса при вводе в 15 строке
first = [int(input(f"{i+1}: ")) for i in range(int(input('Введите кол-во элементов первого массива: ')))]
second = [int(input(i)) for i in range(int(input('Введите кол-во элементов второго массива: ')))]
result = [i for i in first if i not in second]
print(result)