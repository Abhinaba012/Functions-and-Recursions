# Write a function to print factorial of a given number

def factorial(num, factor = 1):
    for den in range(1, num +1):
        factor = factor * den
    return factor
num = 5
print(factorial(num))