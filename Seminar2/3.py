n = int(input('Введите количество дней '))
count = 0
maxCount = 0

for i in range(1, n+1):
    day = int(input(f'{i} день '))
    if day > 0:
        count += 1
        if count>maxCount:
            maxCount = count
    else:
        count = 0
print(f"{maxCount} - наибольшее количество теплых дней подряд")
