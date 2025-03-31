def zad_4_2(_file):
    tab = []
    for line in _file:
        l = line.strip()
        tab += [l]

    x = 0
    napis = []
    for n in range(19, len(tab), 20):
        napis += tab[n][x]
        x += 1
    print(''.join(napis))


file_test = open("pliki_do_zadan/przyklad.txt", "r")
_file = open("pliki_do_zadan/napisy.txt", "r")


print("test:")
zad_4_2(file_test)

print("rozwiązanie:")
zad_4_2(_file)