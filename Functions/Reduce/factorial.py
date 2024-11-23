from functools import reduce
num = 4
print(reduce(lambda v1, v2: v1 * v2, range(1, num + 1)))

#  for factorial of 0

from functools import reduce
num = 0
print(reduce(lambda v1, v2: v1 * v2, range(1, num + 1), 1))
