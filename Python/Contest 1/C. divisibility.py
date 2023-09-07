def divisibility(a, b):
    result = (a % b) * (b % a) + 1
    return result


a = int(input())
b = int(input())

print(divisibility(a, b))
