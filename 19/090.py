def calculate_appetite_remaining(triples):
    results = []

    for triple in triples:
        eaten, need, stock = triple
        total_appetite = eaten + need
        remaining = max(0, stock - eaten)

        results.append([total_appetite, remaining])

    return results

input_data = [[2, 5, 6], [3, 9, 22]]
output = calculate_appetite_remaining(input_data)
print(f"Input: {input_data}")
print(f"Output: {output}")