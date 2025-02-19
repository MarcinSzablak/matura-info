def zad_3_1(_file):
    liczby_potengi = []
    for line in _file:
        l = int(line.strip())
        if (l ** 0.5).is_integer():
            liczby_potengi += [l]
    return liczby_potengi, len(liczby_potengi)

file_test = open("pliki_do_zadan/liczby_przyklad.txt", "r")
file = open("pliki_do_zadan/liczby.txt", "r")

print("zad 3.1:")
print(zad_3_1(file_test))
print(zad_3_1(file))

def is_primary(n):
    for x in range(1,n):
        for y in range(1, int(x**0.5)+1):
            if x % y == 0 and x != y:
                return False
        return True

def zad_3_2(_file):
    liczby = []
    for line in _file:
        l = int(line.strip())
        c = int(line.strip())
        dzielniki = []

        for i in range(2, l+1):
            if is_primary(i):
                while c % i == 0:
                    dzielniki += [i]
                    c = c / i
        if len(set(dzielniki)) >= 5:
            liczby += [l]

    return sorted(liczby)

file_test = open("pliki_do_zadan/liczby_przyklad.txt", "r")
file = open("pliki_do_zadan/liczby.txt", "r")

print("zad 3.2:")
print(zad_3_2(file_test))
print(zad_3_2(file))

def zad_3_3(_file):
    mniejsze = []
    wieksze = []
    rowne = []

    for line in _file:
        l = line.strip()
        wieksza = int(''.join(sorted(list(l))[::-1]))
        mniejsza = int(''.join(sorted(list(l))))

        wynik = wieksza - mniejsza

        l = int(l)

        if wynik > l:
            wieksze += [l]
        elif wynik < l:
            mniejsze += [l]
        else:
            rowne += [l]
    print("wieksze: ", len(wieksze))
    print("mniejsze: ", len(mniejsze))
    print("równe:", len(rowne), rowne)

file_test = open("pliki_do_zadan/liczby_przyklad.txt", "r")
file = open("pliki_do_zadan/liczby.txt", "r")

print("zad 3.3:")
zad_3_3(file_test)
zad_3_3(file)
