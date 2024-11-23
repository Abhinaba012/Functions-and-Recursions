def factorial(num, faact = 1):
    for val in range(1, num+1):
        fact = fact * val
    return fact
def strong(num, res = 0):
    dup = num
    while num != 0:
        rem = num % 10
        res = res + factorial(rem)
        num = num // 10
    return dup == res
print(list(filter(strong, range(100, 200))))