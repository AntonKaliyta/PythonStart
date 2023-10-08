list_poem = [list(i) for i in input().split()]
str_count = len(list_poem)

def a_count(x):
        count_1 = 0
        for j in range(len(list_poem[x])):
            if list_poem[x][j] == 'а':
                count_1 += 1
        return count_1

check = 0
for i in range(1,str_count):
    if a_count(i) == a_count(i-1):
        check += 1

if check == str_count-1:
    print('Парам пам-пам')
else:
    print('Пам парам')




# dictionary = 'аяуюоеёэиы'
# poem = input().split()
# result = [sum([True for i in word.lower() if i in dictionary]) for word in poem]

# if all(result) and len(set(result)) == 1:
#     print('Парам пам-пам')
# else:
#     print('Пам парам')



# count_1 = 0
# count_2 = 0
# for i in range(0, str_count):
#     count_1 = count_2
#     count_2 = 0
#     for j in range(len(list_poem[i])):
#         if list_poem[i][j] == 'а':
#             count_1 += 1
# print(count_1)


# def a_count(list_f):
#     count = 0
#     for i in range(len(list_f)):
#         if list_f[i] == 'а':
#             count += 1
#             return count
    
# print(a_count(list_poem[0]))

# for i in range(len(list_poem)):
#     if list_poem[i] ==  'а' or 'о' or 'и' or 'э' or 'ы' or 'я' or 'ю' or 'е' or 'ё' or 'у':