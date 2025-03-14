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

def check_if_in(x, n, tab):
    for i in range(n):
        if tab[i] == x:
            return True
    return False

def zad_1_3(n):
    if n >= 1000:
        return
    tab = []
    dlugosc_tablicy = 0
    liczba = SumaKwCyfr(n)
    while True:
        if liczba == 1:
            return True

        tab += [liczba]
        dlugosc_tablicy += 1

        liczba = SumaKwCyfr(liczba)
        czy = check_if_in(liczba, dlugosc_tablicy, tab)
        if czy:
            return False