def bin_sqr_sqrt(x, precision=1e-6):
    if x == 0:
        return 0
    elif x < 1:
        left, right = x, 1
    else:
        left, right = 0, x / 2 + 1

    while right - left > precision:
        mid = (left + right) / 2
        mid_squared = mid * mid + mid ** 0.5

        if abs(mid_squared - x) < precision:
            return mid
        elif mid_squared < x:
            left = mid
        else:
            right = mid

    return (left + right) / 2


x = float(input().strip())

sqrt_x = bin_sqr_sqrt(x)

print(f'{sqrt_x:.6f}')
