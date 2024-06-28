import itertools

def find_max_min_products(numbers):
    pairs = list(itertools.combinations(numbers, 2))

    products = [(pair, pair[0] * pair[1]) for pair in pairs]

    max_product_pair = max(products, key=lambda x: x[1])
    min_product_pair = min(products, key=lambda x: x[1])

    return max_product_pair, min_product_pair

numbers = [1, -2, 3, 4, -5, 6]
max_pair, min_pair = find_max_min_products(numbers)

print("Pair with the maximum product:", max_pair[0], "Product:", max_pair[1])
print("Pair with the minimum product:", min_pair[0], "Product:", min_pair[1])