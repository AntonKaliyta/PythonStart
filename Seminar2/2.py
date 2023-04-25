# Каким по счёту в последовательности фибначчи будет заданное число
a = int(input())
x = 0
y = 1
count = 2
while y <= a:
    if y == a:
        print(count)
        break
    x, y = y, x+y
    count += 1
else:
    print(-1)
