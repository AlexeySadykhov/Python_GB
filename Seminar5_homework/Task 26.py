def make_pow(n, pw):
    if n == 0 and pw < 0:
        raise ZeroDivisionError("0 can't be raised to a negative power.")
    if n == 0 and pw == 0:
        return 1
    if n == 0 or n == 1:
        return n
    if pw > 1:
        return n * make_pow(n, pw - 1)
    if pw < 1:
        return 1 / n * make_pow(n, pw + 1)
    return n


print(make_pow(3, 5))
