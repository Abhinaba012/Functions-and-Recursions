# Write a program to check given number is prime or not

def prime(num):
    for den in range(2, num//2 + 1):
        if num % den == 0:
            return "Not Prime"
    return "Prime"
num = 10
print(prime(num))

# Or

def prime_num(n):
    for i in range(2, int(n**0.5)+ 1):
        if n % i == 0:
            return "Not Prime"
    return "Prime"
val = 19
print(prime_num(val))

#  Or

def Prime(val, facount = 0):
    for h in range(1, val + 1):
        if val % h == 0:
            facount += 1
    return facount == 2
val = 10
print("Prime" if prime(val) else "Not Prime")