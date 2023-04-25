n = int(input('Введите кол-во арбузов '))
watermelon = int(input('Укажите массу арбуза '))
max = watermelon
min = watermelon
for i in range(n-1):
    watermelon = int(input('Укажите массу арбуза '))
    if watermelon > max:
        max = watermelon
    elif watermelon < min:
        min = watermelon
print(f'Самый легкий весит {min} кг, самый тяжелый {max}')
