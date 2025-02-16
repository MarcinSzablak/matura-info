from typing import Counter

def zad_4_1(file):
    lines = file.readlines()
    l1 = lines[0].strip().split(" ")
    l2 = lines[1].strip().split(" ")

    counter = 0

    for x in range(len(l1)):
        for y in range(len(l2)):
            if int(l2[y]) % int(l1[x]) == 0:
                counter += 1
                break

    print(counter)

print("zad 4.1:")
file1 = open("pliki_do_zadan/liczby_przyklad.txt")
file2 = open("pliki_do_zadan/liczby.txt")
print("test:", end=" ")
zad_4_1(file1)
print("rozwiązanie:", end=" ")
zad_4_1(file2)

def zad_4_2(file):
    lines = file.readlines()
    l1 = lines[0].strip().split(" ")

    for x in range(len(l1)):
        l1[x] = int(l1[x])

    l1 = sorted(l1)[::-1]

    print(l1[102])

print("zad 4.2:")
file1 = open("pliki_do_zadan/liczby_przyklad.txt")
file2 = open("pliki_do_zadan/liczby.txt")
print("test:", end=" ")
zad_4_2(file1)
print("rozwiązanie:", end=" ")
zad_4_2(file2)

def zad_4_3(file):
    lines = file.readlines()
    l1 = list(map(int, lines[0].strip().split(" ")))
    l2 = list(map(int, lines[1].strip().split(" ")))

    tab = []
    for i in range(len(l2)):
        pomoc = l2[i]
        for j in range(len(l1)):
            if l2[i] % l1[j] == 0:
                l2[i] = l2[i] / l1[j]
        if l2[i] == 1:
            print(pomoc, end=", ")
    print()

print("zad 4.3:")
file1 = open("pliki_do_zadan/liczby_przyklad.txt")
file2 = open("pliki_do_zadan/liczby.txt")
print("test:")
zad_4_3(file1)
print("rozwiązanie:")
zad_4_3(file2)


def zad_4_4(file):
    lines = file.readlines()
    l1 = list(map(int, lines[0].strip().split(" ")))

    return naj_wieksza_srednia(l1)

def naj_wieksza_srednia(lista, min_dla = 50):
    n = len(lista)
    maks_sredna = 0
    maks_start_index = 0
    maks_dla = 0

    for x in range(n - min_dla + 1):
        suma_bez = sum(lista[x:x + min_dla])
        dla_bez = min_dla
        srednia_bez = suma_bez / dla_bez
        if srednia_bez > maks_sredna:
            maks_sredna = srednia_bez
            maks_start_index = x
            maks_dla = dla_bez
        for y in range(x + min_dla, n):
            suma_bez += lista[y]
            dla_bez += 1
            srednia_bez = srednia_bez / dla_bez
            if srednia_bez > maks_sredna:
                maks_sredna = srednia_bez
                maks_start_index = x
                maks_dla = dla_bez

    return maks_sredna, maks_dla ,lista[maks_start_index]

print("zad 4.4:")
file1 = open("pliki_do_zadan/liczby_przyklad.txt")
file2 = open("pliki_do_zadan/liczby.txt")
print("test:", end=" ")
print(zad_4_4(file1))
print("rozwiązanie:", end=" ")
print(zad_4_4(file2))
