# concatenation

def conc(val1, val2):
    return val1 + val2
print(list(map(conc, 'abcd', 'pqrs')))

# Using lambda function

print(list(map(lambda val1, val2: val1 + val2, 'abcd', 'pqrs')))