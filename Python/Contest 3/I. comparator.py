from functools import cmp_to_key
from sys import stdin


def comparator(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0


v = [line.rstrip() for line in stdin]

v.sort(key=cmp_to_key(comparator))

print(''.join(v))
