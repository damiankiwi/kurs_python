def generate_sequence(start, end, step, skip_count):

    for i in range(start, end, step):
        if skip_count > 0:
            yield i
            skip_count -= 1
        else:
            yield "..."
            skip_count = skip_count + step - 1

sequence_generator = generate_sequence(1, 30, 2, 4)

for item in sequence_generator:
    print(item, end=", ")