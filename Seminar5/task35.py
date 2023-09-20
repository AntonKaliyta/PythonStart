# x = int(input('Введите проверяемое число: '))
# for i in range(2,x):
#     if x % i == 0:
#         print('Число составное ')
#         break
# else:
#     print('Число простое')
        



# def isitPrime(k):
#     if k==2 or k==3: return True
#     if k%2==0 or k<2: return False
#     for i in range(3, int(k**0.5)+1, 2):
#         if k%i==0:
#             return False
#     return True
# print(isitPrime(int(input('Введите проверяемое число: '))))




from sympy import isprime
print(isprime(int(input('Введите проверяемое число: '))))