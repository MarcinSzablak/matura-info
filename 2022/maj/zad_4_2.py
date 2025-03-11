def sito(n):
    tab = [True] * n
    tab[0] = tab[1] = False
    for i in range(2, int(n**0.5) + 1):
        if tab[i] == True:
            for j in range(i*i, n, i):
                tab[j] = False

    primes = [i for i in range(n) if tab[i]]

    return primes

def rozdziel(l):
    primes = sito(l)
    x = 0
    tab = []
    while l > 1:
        if x >= len(primes):
            break
        if l % primes[x] == 0:
            l /= primes[x]
            tab += [primes[x]]
            x = 0
        else:
            x += 1
    return tab

def zad_4_2(_file):
    max_dlugosc = (0, 0)
    max_ruznosc = (0, 0)
    for line in _file:
        l = l_copy = int(line.strip())

        dlugosc = rozdziel(l)
        ruznosc = set(dlugosc)

        if len(dlugosc) > max_dlugosc[1]:
            max_dlugosc = (l, len(dlugosc))
        if len(ruznosc) > max_ruznosc[1]:
            max_ruznosc = (l, len(ruznosc))

    return max_dlugosc, max_ruznosc


file_test = open("pliki_do_zadan/przyklad.txt", "r")
file = open("pliki_do_zadan/liczby.txt", "r")

print(zad_4_2(file_test))
print(zad_4_2(file))