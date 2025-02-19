def zad_1_2(n):
    if n == 0:
        return None

    J = []
    b = 1

    while n > 0:
        if n % 2 == 1:
            J += [b]
        n = n // 2
        b += 1

    return J


print(zad_1_2(19))
print(zad_1_2(75))