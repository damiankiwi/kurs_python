def max_profit_one_transaction(prices):
    if not prices or len(prices) < 2:
        return 0

    max_profit = 0
    min_price = prices[0]

    for price in prices[1:]:
        profit = price - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, price)

    return max_profit

stock_prices = [224, 236, 247, 258, 259, 225]
result = max_profit_one_transaction(stock_prices)
print(result)