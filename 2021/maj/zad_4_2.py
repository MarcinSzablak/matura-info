def zad_4_2(_file):
    maks_ciong = 0
    maks_komenda = ""
    ciong = 0
    last = ""
    for line in _file:
        l = line.strip().split()

        if last == l[0]:
            ciong += 1
            if maks_ciong < ciong:
                maks_ciong = ciong
                maks_komenda = l[0]
        else:
            last = l[0]
            ciong = 0

    return maks_komenda, maks_ciong + 1

file_test = open("pliki_do_zadan/przyklad.txt", "r")
file = open("pliki_do_zadan/instrukcje.txt", "r")

wynik_test = zad_4_2(file_test)
wynik = zad_4_2(file)

print(wynik_test)
print(wynik)
