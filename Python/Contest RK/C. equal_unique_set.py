def is_unique_set(set1: set, set2: set) -> str:
    if set1 == set2:
        return "YES"
    return "NO"


n = int(input())
set1 = set(map(int, input().split()))
m = int(input())
set2 = set(map(int, input().split()))

print(is_unique_set(set1, set2))
