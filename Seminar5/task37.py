# def rec(num, count):
#     if count !=0:
#         print(num)
#         return rec(num-1, count-1)

# x = int(input())
# new_count = x     
# rec(x, new_count)

def num_s(n):
    if n == 0:
        return ''
    res = input()
    return num_s(n - 1) + f'{res} '

print(num_s(5))