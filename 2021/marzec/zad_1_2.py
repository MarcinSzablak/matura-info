def to_bin(n):
    binarna = []
    dlugosc_bin = 0
    while n >= 1:
        binarna += [n % 2]
        n = n // 2
        dlugosc_bin += 1

    nowa_binarna = []

    for x in range(dlugosc_bin - 1, -1, -1):
        nowa_binarna += [binarna[x]]

    return nowa_binarna, dlugosc_bin

def zad_1_2(k, x, y):
    runda = 0

    while x != y:
        runda += 1
        x //= 2
        y //= 2

    return runda

print(zad_1_2(5,16,30))