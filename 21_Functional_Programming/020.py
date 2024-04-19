def count_local_variables():
    x = 1
    y = 2
    z = 3

    local_vars = locals()

    count = len(local_vars)

    return count

print(count_local_variables())