letters = [str(i) for i in input('Введите буквы через пробел ').split()]
print(letters)

for i in range(len(letters)):
    count = letters.count(letters[i])
    letters[i] += f"_{count}"

# letters_2 = letters[::-1]
# print(letters_2)

new_letters = list(reversed(letters))
print(new_letters)




# letters = "a a a b c a a d c d d".split()
# for i in range(len(letters)):
#     print(f"{letters[i]}_{letters[0:i].count(letters[i])}")
