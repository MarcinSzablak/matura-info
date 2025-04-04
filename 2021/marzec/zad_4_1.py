def zad_4_1(_file):
    tab = []
    for line in _file:
        l = line.strip().split()
        tab += [l[0]]

    tab_set = set(tab)

    for x in tab_set:
        print(f"{x}: {tab.count(x)}")


file_test = open("pliki_do_zadan/galerie_przyklad.txt", "r")
_file = open("pliki_do_zadan/galerie.txt", "r")

print("test")
zad_4_1(file_test)
print("rozwiącanie")
zad_4_1(_file)
