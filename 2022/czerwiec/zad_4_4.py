def zad_4_4(_file):
    liczby = []
    for line in _file:
        l = int(line.strip())
        liczby += [l]

    liczby_set = set(liczby)

    pary = 0
    trojki = 0

    for x in liczby_set:
        if liczby.count(x) == 2:
            pary += 1
        if liczby.count(x) == 3:
            trojki += 1

    print(len(liczby_set), pary, trojki)


file_test = open("pliki_do_zadan/przyklad.txt", "r")
file = open("pliki_do_zadan/liczby.txt", "r")

print("test:")
zad_4_4(file_test)
print("rozwiązanie")
zad_4_4(file)