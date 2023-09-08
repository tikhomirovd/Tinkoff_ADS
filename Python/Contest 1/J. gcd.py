def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


n = int(input())
numbers = list(map(int, input().split()))

result_gcd = numbers[0]
for num in numbers[1:]:
    result_gcd = gcd(result_gcd, num)

print(result_gcd)
