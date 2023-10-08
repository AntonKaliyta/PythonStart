# def find_farthest_orbit(list_orbits):
#     result = 0
#     res = ''
#     for i in range(len(list_orbits)):
#         if list_orbits[i][0] == list_orbits[i][1]:
#             result = result
#         else:
#             tmp = list_orbits[i][0] * list_orbits[i][1]
#             if tmp > result:
#                 result = tmp
#                 res = orbits[i]
#     return res



import math
def find_farthest_orbit(list_orbits):
    s_orbits = {math.pi * x[0] * x[1]: x for x in orbits if x[0] != x[1]}
    return max(s_orbits.items())[1]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))
