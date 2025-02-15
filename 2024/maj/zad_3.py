from math import gcd

def zad_3_1(n):
    m = 0
    z = 1
    while n > 0:
        cyfra = n % 10
        if cyfra % 2 != 0:
            m = m + cyfra * z
            z *= 10
        n = n // 10

    if m == 0:
        return None

    return m

print("zad 3.1:")
print(zad_3_1(294762))
print(zad_3_1(224))

def zad_3_2(file):
    tab = []
    for line in file:
        l = int(line.strip())
        if zad_3_1(l) == None:
            tab += [l]
    return len(tab),max(tab)

print("zad 3.2:")
file1 = open("pliki_do_zadan/skrot.txt", "r")
print(zad_3_2(file1))

def zad_3_3(file):
    tab = []
    for line in file:
        l = int(line.strip())
        if zad_3_1(l) != None:
            if gcd(zad_3_1(l), l) == 7:
                tab += [l]
    return tab

print("zad 3.3:")
file1 = open("pliki_do_zadan/skrot2.txt", "r")
print(zad_3_3(file1))