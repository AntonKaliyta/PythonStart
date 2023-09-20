# Хакер Василий получил доступ к классному
# журналу и хочет заменить все свои минимальные
# оценки на максимальные. Напишите программу,
# которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.

# мое решение
# low = int(input('Введите низший балл '))
# high = int(input('Введите высший балл '))

# import random as ran
# x = int(input('Введите кол-во оценок '))
# marks = []
# for i in range(x):
#     marks.append(ran.randint(low,high))
# print('оценки: ', marks)

# max_mark = low
# for i in range(len(marks)):
#     if marks[i] > max_mark:
#         max_mark = marks[i]
# print(max_mark)

# min_mark = high
# for i in range(len(marks)):
#     if marks[i] < min_mark:
#         min_mark = marks[i]
# print(min_mark)

# for i in range(len(marks)):
#     if marks[i] == max_mark:
#         marks[i] = min_mark

# print(marks)



# пример работы с map
# def square(num):
#       return num ** 2
# numbers = [1, 2, 3, 4, 5]
# squared = map(square, numbers)
# print(list(squared))

# вариант ввода вручную

# marks = list(map(int, input().split()))
# marks_min, marks_max = min(marks), max(marks)
# for i in range(len(marks)):
#                if marks[i] == marks_max:
#                        marks[i] = marks_min
# print(marks)

# ещё короче(не мой вариант)
marks = list(map(int, input().split()))
marks_min, marks_max = min(marks), max(marks)
result = [i if i != marks_max else marks_min for i in marks]
print(result)