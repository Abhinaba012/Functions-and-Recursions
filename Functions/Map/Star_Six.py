# * * * * * * *
#   * * * * *
#     * * *
#       *

print('\n'.join(list(map(lambda sp, st: sp * '  ' + st * '* ', range(0, 4), range(7, 0, -2)))))

# By using for loop

obj = map(lambda sp, st: sp * '  ' + st * '* ', range(0, 4), range(7, 0, -2))
for st in obj:
    print(st)