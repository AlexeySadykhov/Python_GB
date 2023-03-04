def stupid_sum(a, b):
    if b > 0:
        return stupid_sum(a + 1, b - 1)
    if b < 0:
        return stupid_sum(a - 1, b + 1)
    return a


print(stupid_sum(52, -19))
