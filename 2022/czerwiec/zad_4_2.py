def zad_4_2(_file):
    maks = (0, 0)
    for line in _file:
        l = line.strip()

        liczba = int(l)
        liczba_odwrotna = int(l[::-1])

        bezwzgledna = liczba - liczba_odwrotna

        if bezwzgledna < 0:
            bezwzgledna *= -1

        if bezwzgledna > maks[1]:
            maks = (liczba, bezwzgledna)
    print(maks)



file_test = open("pliki_do_zadan/przyklad.txt", "r")
file = open("pliki_do_zadan/liczby.txt", "r")

print("test:")
zad_4_2(file_test)
print("rozwiązanie")
zad_4_2(file)