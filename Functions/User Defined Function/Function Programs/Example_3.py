# Write a function to compare between two values

def compare(val1, val2):
    if val1 > val2:
        return "val1 is high"
    return "val2 is high"
print(compare(11,22))
print(compare(70,40))


def again_compare(num1, num2):
    if num1 > num2:
        print("num1 is high")
    else:
        print("num2 is high")
compare(11,22)
compare(70,40)