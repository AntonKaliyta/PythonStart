n = int(input())
max_number = n
while n != 0:
    n = int(input())
    if n > max_number:
        max_number = n
print(max_number)