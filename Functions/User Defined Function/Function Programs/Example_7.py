# Write a program to check given number is armstrong or not

def armstrong(num, res = 0):
    power = len(str(num))
    while num != 0:
        rem = num % 10
        res = res + rem ** power
        num = num // 10
    return res
num = 370
print("Armstrong" if armstrong(num) == num else "Not armstrong")
