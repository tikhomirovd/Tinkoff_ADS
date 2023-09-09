def can_become_non_decreasing(n: int, a: list) -> tuple[str, list]:
    result = [min(a[0], -a[0])]

    for i in range(1, n):
        if abs(a[i]) == abs(result[-1]):
            result.append(a[i])
        elif -a[i] > result[-1] and a[i] > result[-1]:
            result.append(min(-a[i], a[i]))
        elif -a[i] > result[-1]:
            result.append(-a[i])
        elif a[i] > result[-1]:
            result.append(a[i])
        else:
            return "No", []

    return "Yes", result


n = int(input())
a = list(map(int, input().split()))

answer, sequence = can_become_non_decreasing(n, a)
print(answer)
if answer == "Yes":
    print(' '.join(map(str, sequence)))
