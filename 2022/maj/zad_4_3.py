def zad_4_3_a(_file):
    liczby = []
    for line in _file:
        l = int(line.strip())
        liczby += [l]

    liczby.sort()
    tab = []

    n = len(liczby)
    for x in range(n):
        a = liczby[x]
        for y in range(x, n):
            b = liczby[y]
            if b % a == 0 and a != b:
                for z in range(y, n):
                    c = liczby[z]
                    if c % b == 0 and b != c:
                        tab += [[liczby[x], liczby[y], liczby[z]]]
    print(len(tab))
    for x in tab:
        print(x)


file_test = open("pliki_do_zadan/przyklad.txt", "r")
file = open("pliki_do_zadan/liczby.txt", "r")

#zad_4_3_a(file_test)
#zad_4_3_a(file)

def zad_4_3_b(_file):
    liczby = []
    for line in _file:
        l = int(line.strip())
        liczby += [l]

    liczby.sort()
    tab = []

    n = len(liczby)
    for x in range(n):
        a = liczby[x]
        for y in range(x, n):
            b = liczby[y]
            if b % a == 0 and a != b:
                for z in range(y, n):
                    c = liczby[z]
                    if c % b == 0 and b != c:
                        for q in range(z, n):
                            d = liczby[q]
                            if d % c == 0 and c != d:
                                for r in range(q, n):
                                    e = liczby[r]
                                    if e % d == 0 and d != e:
                                        tab += [[liczby[x], liczby[y], liczby[z], liczby[q], liczby[r]]]
    print(len(tab))

file_test = open("pliki_do_zadan/przyklad.txt", "r")
file = open("pliki_do_zadan/liczby.txt", "r")

zad_4_3_b(file_test)
zad_4_3_b(file)