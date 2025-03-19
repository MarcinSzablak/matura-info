def sito(n):
    tab = [False, False]
    for x in range(2, n + 1):
        tab += [True]

    for x in range(2, int(n**0.5)+1):
        if tab[x]:
            for y in range(x * x, n + 1, x):
                tab[y] = False

    return [x for x in range(2, n + 1) if tab[x]]

def goldbach(l, pierwsze):
    counter = 0
    for prime in pierwsze:
        if prime > l // 2:
            break
        if (l - prime) in pierwsze:
            counter += 1
    print(l)
    return counter

def zad_3_3(_file):
    maks = (0, 0)
    min = (0, 0)
    tab = []
    for line in _file:
        l = int(line.strip())

        tab += [l] 

    maks_liczba = max(tab)

    pierwsze = sito(maks_liczba)

    for l in tab:
        liczba_par =  goldbach(l, pierwsze)

        if maks[1] < liczba_par:
            maks = (l, liczba_par)

        if min == (0, 0) or min[1] > liczba_par:
            min = (l, liczba_par)

    return(maks, min)

file_test = open("pliki_do_zadan/liczby_przyklad.txt", "r")
file = open("pliki_do_zadan/liczby.txt", "r")

print("test: ", zad_3_3(file_test))

print("rozwiązanie: ", zad_3_3(file))
