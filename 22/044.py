def extract_non_zero_blocks(input_list):
    non_zero_blocks = []
    current_block = []

    for num in input_list:
        if num != 0:
            current_block.append(num)
        else:
            if current_block:
                non_zero_blocks.append(current_block)
                current_block = []

    if current_block:
        non_zero_blocks.append(current_block)

    return non_zero_blocks

input_list = [1, 2, 0, 3, 4, 0, 5, 6, 7, 0, 8]
non_zero_blocks = extract_non_zero_blocks(input_list)
print(f"Non-zero blocks: {non_zero_blocks}")