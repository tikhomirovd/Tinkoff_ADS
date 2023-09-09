def prime_factors(n: int):
    while n % 2 == 0:
        print(2, end=' ')
        n //= 2

    i = 3
    while i * i <= n:
        while n % i == 0:
            print(i, end=' ')
            n //= i
        i += 2

    if n > 2:
        print(n)


n = int(input())
prime_factors(n)
