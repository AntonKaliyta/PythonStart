array = [0, -1, 5, 2, 3]
print(array)
result_array = []

for i in range(len(array)-1):
    if array[i+1] > array[i]:
        result_array.append(array[i+1])
print(result_array)
