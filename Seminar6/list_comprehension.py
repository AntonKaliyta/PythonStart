# squares = [i ** 2 for i in range(10)]
# print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# в развернутом виде:
# squares = []
# for x in range(10):
#   squares.append(x ** 2)
# print(squares)


# squares = [i * 3 for i in range(1,10,2)]
# print(squares)
# [3, 9, 15, 21, 27]

# nums = [i for i in range(20) if i % 2 != 0]
# print(nums)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# nums = [i for i in range(100) if i%10 == 0]
# print(nums)
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# nums = [i for i in range(100) if i%10 == 0 and i//10 > 5 ]
# print(nums)
# [60, 70, 80, 90]

# nums = [i ** 2 if i % 2 == 0 else i ** 3 for i in range(10)]
# print(nums)
# [0, 1, 4, 27, 16, 125, 36, 343, 64, 729]

# nums = [i ** 2 if i % 2 == 0 else i  for i in range(10)]
# print(nums)
# [0, 1, 4, 3, 16, 5, 36, 7, 64, 9]


# first = []
# for x in range(1, 5):
#   for y in range(5, 1, -1):
#     if x != y:
#       first.append((x, y))
# second = [(x, y) for x in range(1, 5) for y in range(5, 1, -1) if x != y]
# print(first == second)
# True

# vec = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# vec = [digit for lst in vec for elem in lst for digit in elem]
# print(vec)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
