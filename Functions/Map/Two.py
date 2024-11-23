# Even_Odd

# Using TypeCasting
def even_odd(num):
    if num % 2 == 0:
        return 'even'
    return'odd'
print(list(map(even_odd, [11, 21, 22, 35, 36, 98])))

# Using For loop

def even_odd(num):
    if num % 2 == 0:
        return 'even'
    return'odd'
obj = map(even_odd, [11, 21, 22, 35, 36, 98])
for ele in obj:
    print(ele)

# Using lambda function

print(list(map(lambda val: "Even" if val % 2 == 0 else "Odd", [11, 21, 22, 35, 36, 98])))