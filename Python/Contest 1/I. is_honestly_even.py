def is_honestly_even(num: int) -> bool:
    for digit in str(num):
        if int(digit) % 2 != 0:
            return False
    return True


n = int(input())
count = 0

for i in range(1, n + 1):
    if is_honestly_even(i):
        count += 1

print(count)
