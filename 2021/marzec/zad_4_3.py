def zad_4_3(_file):
    maks = ('', 0)
    mini = ('', 0)
    for line in _file:
        l = line.strip().split()
        miasto = l[1]
        wymiary = []
        for x in range(2, len(l), 2):
            if l[x] == '0' or l[x + 1] == '0':
                break
            wymiary += [int(l[x]) * int(l[x + 1])]

        if len(set(wymiary)) > maks[1]:
            maks = (miasto, len(set(wymiary)))

        if mini[1] == 0:
            mini = (miasto, len(set(wymiary)))
        elif  len(set(wymiary)) < mini[1]:
            mini = (miasto, len(set(wymiary)))


    print(maks[0], maks[1])
    print(mini[0], mini[1])

file_test = open("pliki_do_zadan/galerie_przyklad.txt", "r")
_file = open("pliki_do_zadan/galerie.txt", "r")

print("test")
zad_4_3(file_test)
print("rozwiązanie")
zad_4_3(_file)