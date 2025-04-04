def zad_4_2(_file):
    maks = ('', 0)
    mini = ('', 0)
    for line in _file:
        l = line.strip().split()
        miasto = l[1]
        wymiary = 0
        lokale = 0
        for x in range(2, len(l), 2):
            if l[x] == '0' or l[x + 1] == '0':
                break
            wymiary += int(l[x]) * int(l[x + 1])
            lokale += 1

        if wymiary > maks[1]:
            maks = (miasto, wymiary)

        if mini[1] == 0:
            mini = (miasto, wymiary)
        elif wymiary < mini[1]:
            mini = (miasto, wymiary)

        print(miasto, wymiary, lokale)
    print(maks)
    print(mini)

file_test = open("pliki_do_zadan/galerie_przyklad.txt", "r")
_file = open("pliki_do_zadan/galerie.txt", "r")

print("test")
zad_4_2(file_test)
print("rozwiązanie")
zad_4_2(_file)