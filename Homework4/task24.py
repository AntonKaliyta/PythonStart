import random

n = int(input('Введите кол-во грядок: '))
garden = list()
for i in range(n):
    garden.append(random.randint(1,9))

print(garden)

max_berry = 0

for i in range(n):
    temp = garden[i-2] + garden[i-1] + garden[i]
    if temp > max_berry:
        max_berry = temp
print(max_berry)