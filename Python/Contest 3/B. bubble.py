def bubble_sort(n: int, arr: list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):

            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        n -= 1
    return arr


n = int(input())
arr = list(map(int, input().split()))

sorted_arr = bubble_sort(n, arr)

print(" ".join(map(str, sorted_arr)))
