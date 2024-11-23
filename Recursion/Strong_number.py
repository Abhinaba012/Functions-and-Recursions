def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
def strong(val):
    if val == 0:
        return 0
    return factorial(val % 10) + strong(val // 10)
num = 146
print("Strong Number" if strong(num) == num else "Not a Strong Number") 