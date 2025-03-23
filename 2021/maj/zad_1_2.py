def zad_1_2(n):
    jednoscy = 1

    kopia_n = n

    while kopia_n > 1:
        jednoscy  *= 10
        kopia_n = kopia_n / 10

    d = (jednoscy  - 1) - n
    return  d

print(zad_1_2(5000))