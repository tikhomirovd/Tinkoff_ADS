def find_swaps(n: int, arr: list) -> tuple[int, int]:
    a, b = -1, -1
    suma = 0
    for i, elem in enumerate(arr):
        if elem % 2 == 0:
            if (i + 1) % 2 != 0:
                a = i + 1
                suma += 1

        if elem % 2 != 0:
            if (i + 1) % 2 == 0:
                b = i + 1
                suma += 1

    if suma == 2 and a != -1 and b != -1:
        return a, b

    if suma == 0 and n >= 3:
        return 1, 3

    else:
        return -1, -1


n = int(input())
arr = list(map(int, input().split()))

print(*find_swaps(n, arr))
