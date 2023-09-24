
from random import randint

# array = [(randint(1,5)) for i in range(int(input('Введите длину массива: ')))]
# print(array)
# result = [i for i in array if i > array[i+1] and i > array[i-1]]
# print(len(result))





array = [(randint(1,5)) for i in range(int(input('Введите длину массива: ')))]
print(array)
result = [i for i in range(1, len(array) - 1) if array[i+1] < array[i] > array[i-1]]
print(len(result))