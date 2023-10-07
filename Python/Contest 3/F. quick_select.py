import random


def quick_select(arr, low, high, k):
    if low <= high:
        pivot_index = random.randint(low, high)
        pivot_index = partition(arr, low, high, pivot_index)

        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index > k:
            return quick_select(arr, low, pivot_index - 1, k)
        else:
            return quick_select(arr, pivot_index + 1, high, k)
    return arr[k]


def partition(arr, low, high, pivot_index):
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


n, k = map(int, input().split())
arr = list(map(int, input().split()))

element = quick_select(arr, 0, n - 1, k - 1)

print(element)
