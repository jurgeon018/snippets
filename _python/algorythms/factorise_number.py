def factorize_number(x):
    d = 2
    while x > 1:
        if x % d == 0:
            print(d)
            x //= d
        else:
            d += 1


print(factorize_number(999))
