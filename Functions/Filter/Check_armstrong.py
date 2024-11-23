def armstrong(num):
    dup = num
    res = 0
    power = len(str(num))
    while num != 0:
        rem = num % 10
        res = res + rem ** power
        num = num // 10
    return res == dup
print(list(filter(armstrong, range(1, 50))))
