k = int(input('Введите положительное число  '))

list_1 = [1,2,3,4,5]

# for i in range(k):
#     list_1.insert(0,list_1[-1])
#     list_1.pop(-1)
    
for i in range(k):
    list_1.insert(0, list_1.pop())    # можно даже так сократить, т.к. pop возвращает и удаляет значение

print(list_1)

# послание
# послание в ответ
