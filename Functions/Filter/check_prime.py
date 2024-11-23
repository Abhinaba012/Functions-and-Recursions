def prime(num):
    for den in range(2, (num //2) + 1):
        if num % den == 0:
            return False
    return True
print(list(filter(prime, range(10, 21))))

# Or

def prime_num(val, facount = 0):
    for den1 in range(1, val + 1):
        if val % den1 == 0:
            facount += 1
    return facount == 2
print(list(filter(prime_num, range(10, 20))))