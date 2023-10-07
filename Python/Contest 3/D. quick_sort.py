import random


def quick_sort(arr: list, low: int, high: int):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr: list, low: int, high: int):
   # pivot_index = random.randint(low, high)
    pivot_index = (low + high) // 2
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


n = int(input())
arr = list(map(int, input().split()))

quick_sort(arr, 0, n - 1)

print(" ".join(map(str, arr)))
