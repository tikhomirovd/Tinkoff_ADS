def matrix_mult(a, b):
    return (
        a[0] * b[0] + a[1] * b[2], a[0] * b[1] + a[1] * b[3],
        a[2] * b[0] + a[3] * b[2], a[2] * b[1] + a[3] * b[3]
    )


def matrix_pow(matrix, n):
    result = (1, 0, 0, 1)
    while n:
        if n % 2:
            result = matrix_mult(result, matrix)
        matrix = matrix_mult(matrix, matrix)
        n //= 2
    return result


def fast_fibonacci(n):
    if n == 0:
        return 0
    result_matrix = matrix_pow((1, 1, 1, 0), n - 1)
    return result_matrix[0]


n = int(input())
print(fast_fibonacci(n))
