# Write a function to check given number is disarium or not

def disarium(num, res = 0):
    power = len(str(num))
    while num != 0:
        rem = num % 10
        res = res + rem ** power
        num = num // 10
        power = power - 1
    return res
num = 135
print("Disarium" if disarium(num) == num else "Not disarium")