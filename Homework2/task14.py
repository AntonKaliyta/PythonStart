# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input())
result = 2
i = 1
while result <n:
    print(result)
    result = 2**i
    i+=1