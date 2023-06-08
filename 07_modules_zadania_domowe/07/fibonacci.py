def fibonacci_sequence(n):
    result = [0, 1]
    while len(result) <= n:
        next_number = result[-1] + result[-2]
        result.append(next_number)
    return result[:n + 1]