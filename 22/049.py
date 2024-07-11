def filter_empty_strings(strings):
    return list(filter(lambda s: s != '', strings))

strings = ['Hello', '', 'World', '', 'Python', '', 'Programming']
filtered_strings = filter_empty_strings(strings)
print(f"Filtered strings: {filtered_strings}")