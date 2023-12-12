def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

input1 = [8, 10, 7, 5, 7, 15]
output1 = max_profit(input1)
print(output1)

input2 = [1, 2, 8, 1]
output2 = max_profit(input2)
print(output2)

input3 = []
output3 = max_profit(input3)
print(output3)