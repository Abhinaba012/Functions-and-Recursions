# integer to binary----->> range(10,21)

def binary(num, pos = 1, res = 0):
    while num != 0:
            rem = num % 2
            res = res + rem * pos
            pos  = pos * 10
            num = num // 2
    return res
print(list(map(binary, range(10,21))))