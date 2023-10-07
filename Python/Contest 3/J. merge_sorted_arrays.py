import heapq


def merge_sorted_arrays(arrays):
    heap = []
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    result = []
    while heap:
        val, arr_idx, ele_idx = heapq.heappop(heap)
        result.append(val)

        if ele_idx + 1 < len(arrays[arr_idx]):
            next_tuple = (arrays[arr_idx][ele_idx + 1], arr_idx, ele_idx + 1)
            heapq.heappush(heap, next_tuple)

    return result


K = int(input())
arrays = [list(map(int, input().split())) for _ in range(K)]

merged_array = merge_sorted_arrays(arrays)
print(" ".join(map(str, merged_array)))
