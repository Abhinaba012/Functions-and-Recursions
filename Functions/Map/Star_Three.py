# * * * *
#   * * *
#     * *
#       *

print('\n'.join(list(map(lambda sp, st: sp * '  ' + st * "* ", range(0, 4), range(4, 0, -1)))))

# By Using for loop

obj = map(lambda sp, st: sp * '  ' + st * "* ", range(0, 4), range(4, 0, -1))
for st in obj:
    print(st)