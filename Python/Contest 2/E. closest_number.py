def closest_number(arr: list, num: int):
    left, right = 0, len(arr) - 1
    closest_num = None

    while left <= right:
        mid = (left + right) // 2
        if closest_num is None:
            closest_num = arr[mid]
        else:
            closest_num = min(arr[mid], closest_num, key=lambda x: (abs(x - num), x))

        if arr[mid] < num:
            left = mid + 1
        elif arr[mid] > num:
            right = mid - 1
        else:
            return arr[mid]

    return closest_num


n, k = map(int, input().split())
first_array = list(map(int, input().split()))
second_array = list(map(int, input().split()))

for num in second_array:
    print(closest_number(first_array, num))
