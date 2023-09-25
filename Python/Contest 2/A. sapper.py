def print_minesweeper_field(n: int, m: int, mines: list):
    field = [[0 for _ in range(m)] for _ in range(n)]

    # Размещение мин на поле
    for mine in mines:
        x, y = mine
        field[x - 1][y - 1] = '*'

    for i in range(n):
        for j in range(m):
            if field[i][j] == '*':
                continue

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if 0 <= i + dx < n and 0 <= j + dy < m and field[i + dx][j + dy] == '*':
                        field[i][j] += 1

    for row in field:
        print(' '.join(str(cell) for cell in row) + ' ')


N, M = map(int, input().split())
W = int(input())
mines = [tuple(map(int, input().split())) for _ in range(W)]

print_minesweeper_field(N, M, mines)
