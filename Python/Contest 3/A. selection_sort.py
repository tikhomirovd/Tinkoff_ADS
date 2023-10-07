def selection_sort(n: int, arr: list):
    for i in range(n - 1, 0, -1):
        max_index = 0

        for j in range(1, i + 1):
            if arr[j] > arr[max_index]:
                max_index = j

        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr


n = int(input())
arr = list(map(int, input().split()))

sorted_arr = selection_sort(n, arr)

print(" ".join(map(str, sorted_arr)))
