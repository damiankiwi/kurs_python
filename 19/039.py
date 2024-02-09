def triples_sum_to_zero(matrix):
    def is_zero_sum(triple):
        return sum(triple) == 0

    return [is_zero_sum(triple) for triple in matrix]

input1 = [[1343532, -2920635, 332], [-27, 18, 9], [4, 0, -4], [2, 2, 2], [-20, 16, 4]]
output1 = triples_sum_to_zero(input1)
print(f"Input: {input1}\nOutput: {output1}")

input2 = [[1, 2, -3], [-4, 0, 4], [0, 1, -5], [1, 1, 1], [-2, 4, -1]]
output2 = triples_sum_to_zero(input2)
print(f"\nInput: {input2}\nOutput: {output2}")