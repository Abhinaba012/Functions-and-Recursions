# Create two user defined list and add them

# L1 = list(map(int, input().split()))
# L2 = list(map(int, input().split()))
# print(list(map(lambda c1, c2: c1 + c2, L1, L2)))
# print(L1)
# print(L2)

# By using user defined function

def add_list(v1, v2):
    return v1 + v2
print(list(map(add_list, [1,2,3],[5,6,7])))