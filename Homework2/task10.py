# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input('Введите кол-во моент '))
# upCount = 0
# downCount = 0
# for i in range(n):
#     x = input('Укажите, какой сторой вверх лежит следующая монета ')
#     if x == 'герб' or x == 'гербом':
#         upCount+=1
#     elif x == 'решка' or x == 'решкой':
#         downCount+=1
# min = downCount
# if upCount<min:
#     min = upCount
# print(f'Кол-во монет которые необходимо перевернуть равно {downCount}')

# или

n = int(input('Введите кол-во моент '))
upCount = 0
downCount = 0
for i in range(n):
    x = int(input('Укажите, какой сторой вверх лежит следующая монета(0 - решкой, 1 - гербом '))
    if x == 0:
        upCount += 1
    elif x == 1:
        downCount += 1
min = downCount
if upCount < min:
    min = upCount
print(f'Кол-во монет которые необходимо перевернуть равно {min}')

