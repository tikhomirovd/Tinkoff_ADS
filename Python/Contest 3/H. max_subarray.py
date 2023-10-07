def max_subarray_sum(arr):
    max_sum = current_sum = arr[0]
    best_start = best_end = current_start = 0

    for current_end in range(1, len(arr)):
        if current_sum < 0:
            current_start = current_end
            current_sum = arr[current_end]
        else:
            current_sum += arr[current_end]

        if current_sum > max_sum:
            max_sum = current_sum
            best_start = current_start
            best_end = current_end

    return best_start + 1, best_end + 1, max_sum


n = int(input())
arr = list(map(int, input().split()))

start, end, max_sum = max_subarray_sum(arr)

print(start, end, max_sum)
