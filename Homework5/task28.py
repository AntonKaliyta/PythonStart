# Написать рекурсивную функцию sum(a,b), возвращающую сумму двух целых неотрицательных чисел. Арифм операции -1 и +1

# def S(x, y):
#     if (y == 0):
#         return x
#     else:
#         return S(x+1, y-1)


# a = int(input('Введите А '))
# b = int(input('Введите B '))

# print(S(a, b))


def num_sum(x, y):
    if y == 0:
        return x
    else:
        return num_sum(x + 1, y - 1)


a = int(input('Введите А '))
b = int(input('Введите B '))

print(num_sum(a, b))
