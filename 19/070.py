def find_first_negative_balance(transactions):
    balances = [0]

    for transaction_list in transactions:
        current_balance = balances[-1]
        for amount in transaction_list:
            current_balance += amount
            balances.append(current_balance)

    for i, balance in enumerate(balances):
        if balance < 0:
            account_index = i // len(transactions[0])
            transaction_index = i % len(transactions[0])

            if account_index < len(transactions) and transaction_index < len(transactions[0]):
                return [balance, transactions[account_index][transaction_index]]

    return [None, None]


transactions1 = [[12, -7, 3, -89, 14, 88, -78], [-1, 2, 7]]
transactions2 = [[1200, 100, -900], [100, 100, -2400]]

output1 = find_first_negative_balance(transactions1)
output2 = find_first_negative_balance(transactions2)

print(f"Output 1: {output1}")
print(f"Output 2: {output2}")