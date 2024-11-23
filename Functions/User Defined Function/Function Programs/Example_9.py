# Write a function to check given number is palindrome or not

def palindrome(num, res = 0):
    while num != 0:
        rem = num % 10
        res = res * 10 + rem
        num = num // 10
    return res
num = 1221
print("Palindrome" if palindrome(num) == num else "Not Palindrome")
