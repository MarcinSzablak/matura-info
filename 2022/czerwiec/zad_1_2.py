def SumaKwCyfr(n):
    k = 1

    while n>=k:
        k *= 10
        n / 10
    k /= 10

    liczba = 0

    while k >= 1:
        liczba += (n // k)**2
        n -= k * (n // k)
        k /= 10

    return liczba

print(SumaKwCyfr(82))