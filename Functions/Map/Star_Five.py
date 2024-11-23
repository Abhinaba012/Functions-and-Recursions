#       *
#     * * *
#   * * * * *
# * * * * * * *

print('\n'.join(list(map(lambda sp, st: sp * '  ' + st * '* ', range(3, -1, -1), range(1, 8, 2)))))

# By using for loop

bc = map(lambda sp, st: sp * '  ' + st * '* ', range(3, -1, -1), range(1, 8, 2))
for stars in bc:
    print(stars)