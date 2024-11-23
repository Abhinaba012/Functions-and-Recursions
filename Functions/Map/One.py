# Using For Loop

def mult(ch):
    return ch * 3
obj = map(mult, 'abcd')
for ele in obj:
    print(ele)

# Using TypeCasting

def mul(ch):
    return ch * 3
print(list(map(mul, 'abcd')))

# Using lambda Function

print(list(map(lambda val: val * 3, 'abcd')))