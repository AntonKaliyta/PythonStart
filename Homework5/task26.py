# программа принимает два числа и возводит А в целую степень В с помощью рекурсии

def my_pow(num, power):
    if (power == 1):
        return num
    else:
        return num * pow(a, power-1)

a = int(input('Введите число А '))
b = int(input('Введите число B '))

print(pow(a,b))