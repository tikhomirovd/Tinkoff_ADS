def maximum(a: int, b: int) -> int:
    return a * (1 % (a // b + 1)) + b * (1 % (b // (a + 1) + 1))


a = int(input())
b = int(input())

print(maximum(a, b))
