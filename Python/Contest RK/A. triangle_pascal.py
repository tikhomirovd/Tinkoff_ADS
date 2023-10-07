def triangle_pascal(n: int, m: int) -> list:
    arr = [[1 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                pass
            else:
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
    return arr


n, m = map(int, input().split())

arr = triangle_pascal(n, m)
for row in arr:
    print(*row)