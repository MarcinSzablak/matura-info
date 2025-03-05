def silnia(n):
    wynik = 1
    for x in range(1, n+1):
        wynik *= x
    return wynik

def znajdz_maks_kombinacji(n):
    maks = 0
    for x in range(n+1):
        wynik = silnia(n) / (silnia(x) * silnia(n - x))
        if wynik > maks:
            maks = wynik
    return maks

def zad_3_2(file):
    dlugosc_szukana = 8
    maks = znajdz_maks_kombinacji(dlugosc_szukana - 1)
    for line in file:
        l = line.strip()
        if len(l) == dlugosc_szukana:
            liczba_1 = l.count("1") - 1

            k =  dlugosc_szukana - liczba_1

            wynik = silnia(dlugosc_szukana - 1) / (silnia(liczba_1) * silnia(dlugosc_szukana - 1 - liczba_1))
            if wynik == maks:
                print(l)


file_test = open("pliki_do_zadan/DANE_M/przyklad.txt","r")
file = open("pliki_do_zadan/DANE_M/anagram.txt","r")

zad_3_2(file_test)
print("wynik:")
zad_3_2(file)