letters = [str(i) for i in input('Введите буквы через пробел ').split()]

dict_letters = {}.fromkeys(letters, 0)

for i in letters:
    if dict_letters[i] != 0:
        print(f"{i}_{dict_letters[i]}", end=" ")
    else:
        print(i, end=" ")
    dict_letters[i] +=1