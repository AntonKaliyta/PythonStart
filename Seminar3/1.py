# num_list = [1, 1, 2, 0, -1, 3, 4, 4]

num_list = []
for i in range(int(input())):
    num_list.append(input())

# num_list = [input() for i in range(8)]

print(len(set(num_list)))
