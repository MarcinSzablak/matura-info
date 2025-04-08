def sito(n):
    tab = [True] * n
    tab[0] = tab[1] = False

    for x in range(2, int(n ** 0.5) + 1):
        for y in range(x, n, x):
            if x != y:
                tab[y] = False

    pierwsze = []

    for x in range(len(tab)):
        if tab[x] == True:
            pierwsze += [x]

    return pierwsze

def zad_4_1(_file):
    liczby_parzyste = []
    for line in _file:
        l = line.strip().split()
        liczba = int(l[0])
        if liczba % 2 == 0:
            liczby_parzyste += [liczba]

    pierwsze = sito(max(liczby_parzyste))

    for parzysta in liczby_parzyste:
        kombinacje = []
        for a in pierwsze:
            for b in pierwsze:
                if a < b:
                    break
                if a + b < parzysta:
                    continue
                if a + b == parzysta:
                    kombinacje += [(a,b)]
                if a + b > parzysta:
                    break

        maks_k = kombinacje[0]
        maks = maks_k[0] - maks_k[1]

        for k in kombinacje:
            if maks < k[0] - k[1]:
                maks = k[0] - k[1]
                maks_k = k
        print(parzysta, maks_k[0], maks_k[1])

plik_test = open("pliki_do_zadan/przyklad.txt", "r")
plik = open("pliki_do_zadan/pary.txt", "r")

print("test:")
zad_4_1(plik_test)
print("rozwiązanie:")
zad_4_1(plik)