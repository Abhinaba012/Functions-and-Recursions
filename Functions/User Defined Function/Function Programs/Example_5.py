# Write a function to add all the digits from a given number

def add(num, res = 0):
    while num != 0:
        rem = num % 10
        res = res + rem
        num = num // 10
    return res
print(add(1234))

# Write a function to multiple all the digits from a given number

def mul(val, ans = 1):
    while val != 0:
        rem = val % 10
        ans = ans * rem
        val = val // 10
    return ans
print(mul(1234))