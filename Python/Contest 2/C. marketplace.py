def calculate_discounted_price(n: int, prices: list):
    prices.sort(reverse=True)

    total_price = 0
    for i in range(0, n, 3):

        if i + 2 < n:
            total_price += prices[i] + prices[i + 1]

        elif i + 1 < n:
            total_price += prices[i] + prices[i + 1]

        else:
            total_price += prices[i]

    return total_price


n = int(input().strip())
prices = list(map(int, input().strip().split()))

discounted_price = calculate_discounted_price(n, prices)
print(discounted_price)
