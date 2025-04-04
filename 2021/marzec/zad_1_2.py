def zad_1_2(k, x, y):
    runda = 0

    while x != y:
        runda += 1
        x //= 2
        y //= 2

    return runda

print(zad_1_2(5,16,30))