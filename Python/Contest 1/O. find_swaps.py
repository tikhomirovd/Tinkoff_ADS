n = int(input())
arr = list(map(int, input().split()))


def find_swap(arr):
    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] % 2 == 1:  # нечетная позиция, четное число
            for j in range(1, len(arr), 2):  # ищем нечетное число на четной позиции
                if arr[j] % 2 == 0:
                    return i + 1, j + 1
        elif i % 2 == 1 and arr[i] % 2 == 0:  # четная позиция, нечетное число
            for j in range(0, len(arr), 2):  # ищем четное число на нечетной позиции
                if arr[j] % 2 == 1:
                    return i + 1, j + 1
    return -1, -1


i, j = find_swap(arr)
if i == -1:
    print("-1 -1")
else:
    print(i, j)
