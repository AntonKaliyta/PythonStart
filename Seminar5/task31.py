# Фибоначчи через рекурсию

# array = list()
# n = int(input())
# for i in range(n):
#     array.append(0)
# array[0] = 0
# array[1] = 1
# i = 2

# def fib(n, array):
#     if (i == n):
#         return array[i]
#     else:
#         array[i] = array[i-1] + fib(n)
#         i+=1
#         return fib(n)


# def fib(n, array):
#     if i < n:




def fib(n):
    res = 0
    if n in [1, 2]:
        return 1
    return fib(n-2) + fib(n-1)

num = int(input())
print(fib(num))