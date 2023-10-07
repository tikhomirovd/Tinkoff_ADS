def kth_element(k):
    i = j = 1

    count = 0

    while True:
        a_i = i ** 2
        b_j = j ** 3

        if a_i == b_j:
            count += 1
            if count == k:
                return a_i
            i += 1
            j += 1

        elif a_i < b_j:
            count += 1
            if count == k:
                return a_i
            i += 1

        else:
            count += 1
            if count == k:
                return b_j
            j += 1


k = int(input())

element = kth_element(k)

print(element)
