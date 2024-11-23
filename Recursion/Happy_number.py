def sq(val):
    if val == 0:
        return 0
    return (val % 10) ** 2 + sq(val // 10)
def Happy(n):
    if n < 10:
        return n
    return Happy(sq(n))

num = 19
Happy(num)
v = Happy(num) 
print("Happy number" if v ==1 or v == 7 else "Not a Happy Number")