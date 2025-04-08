def zad_4_3(_file):
    pary = []
    for line in _file:
        l = line.strip().split()
        liczba  = int(l[0])
        slowo = l[1]

        if liczba == len(slowo):
            pary += [(liczba, slowo)]
    print(pary)


plik_test = open("pliki_do_zadan/przyklad.txt", "r")
plik = open("pliki_do_zadan/pary.txt", "r")

print("test:")
zad_4_3(plik_test)
print("rozwiązanie:")
zad_4_3(plik)