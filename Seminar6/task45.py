# все делители числа 284
# 220 = 1 + 2 + 4 + 71 + 142
# все делители числа 220
# 284 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110

# k = int(input())


def summa(x):
    result = 0
    x = int(x)
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            result += i
    return result

k = int(input())
for i in range(1, k):
    j = summa(i)
    if i < j < k and i == summa(j):
        print(i, j)

