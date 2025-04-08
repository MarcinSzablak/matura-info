def zad_4_2(_file):
    for line in _file:
        l = line.strip().split()
        slowo = l[1]

        maks_ciong = []
        for x in range(len(slowo)):
            ciong = []
            for y in range(x, len(slowo)):
                if slowo[x] != slowo[y]:
                    break
                ciong += slowo[y]
                if len(ciong) > len(maks_ciong):
                    maks_ciong = ciong
        print("".join(maks_ciong), len(maks_ciong))

plik_test = open("pliki_do_zadan/przyklad.txt", "r")
plik = open("pliki_do_zadan/pary.txt", "r")

print("test:")
zad_4_2(plik_test)
print("rozwiązanie:")
zad_4_2(plik)