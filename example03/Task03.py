# 3 Самая далекая планета
# Подсказка: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь. 

import math
def find_farthest_orbit(orb):
    return max([((math.pi * x[0] * x[1]), x) for x in orb if x[0] != x[1]])[1]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))