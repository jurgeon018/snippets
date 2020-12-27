# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
def euler1():
    sum = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)


# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
def euler2():
    a, b = 0, 1
    sum = 0
    while a < 4000000:
        a, b = b, a+b
        if a % 2 == 0:
            sum += a
    print(sum, end=' ')


def euler3():
    def is_prime(n):
        if n == 1:
            return False
        for d in range(2, n):
            if n % d == 0:
                return False
        return True
    divs_list = []
    for n in range(1, 20):
        if is_prime(n):
            divs_list.append(n)
    # max_divison = max(divisors_list)
    print(divs_list)


print(euler3())
