def even(val):
    if val % 2 == 0:
        return True
print(list(filter(even, range(1, 10))))