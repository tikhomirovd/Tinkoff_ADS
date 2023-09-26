def bin_xerox(n: int, x: int, y: int) -> int:
    left, right = 0, n * max(x, y)

    while left < right:
        mid = (left + right) // 2
        copies = mid // x + mid // y + 1

        if copies >= n:
            right = mid
        else:
            left = mid + 1

    return left


n, x, y = map(int, input().split())

time = bin_xerox(n, x, y)

print(time)
