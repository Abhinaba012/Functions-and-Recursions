#       *
#     * *
#   * * *
# * * * *

print('\n'.join(list(map(lambda sp, st: sp * "  " + st * '* ', range(3, -1, -1), range(1, 5)))))

# By using for loop

mf = map(lambda sp, st: sp * "  " + st * '* ', range(3, -1, -1), range(1, 5))
for star in mf:
    print(star)
