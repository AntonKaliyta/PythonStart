# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.


# word = input('Введите слово: ').upper()

# word = 'ADAA'
# arr_word = list(word)
# length = len(arr_word)
# count = 0
# i = 0
# for i in  range(length):
#     if arr_word[i] == 'A' or 'E' or 'I' or 'O' or 'U' or 'L' or 'N' or 'S' or 'T' or 'R':
#         count+=1
#     elif arr_word[i] == 'D' or 'G':
#         count+=2
# print(count)
# так и не хочет совпадение засчитывать за 2 очка, за любой символ дает 1 балл, даже за цифры. 

# A, E, I, O, U, L, N, S, T, R = 1
# # D, G = 2

# word = int(word)
# result = [int(word) for i in range(len(word))]


letter = {1:'AEIOULNSTRАВЕИНОРСТ',
      	2:'DGДКЛМПУ',
      	3:'BCMPБГЁЬЯ',
      	4:'FHVWYЙЫ',
      	5:'KЖЗХЦЧ',
      	8:'JZШЭЮ',
      	10:'QZФЩЪ'}

word = input('Введите слово: ').upper()
print('За это слово вы получаете', sum([k for i in word for k, v in letter.items() if i in v]), 'очков')
