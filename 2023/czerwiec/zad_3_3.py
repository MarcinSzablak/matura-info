def to_bin(n):
    binary = []
    while n >= 1:
        binary += [f"{n % 2}"]
        n = n // 2
    return binary[::-1]

def zad_3_3(file):
    maks = 0
    tab = []
    for line in file:
        l = line.strip()
        tab += [l]

    for x in range(len(tab)):
        if x + 1 >= len(tab) - 1:
            break
        y1 = int(tab[x], 2)
        y2 = int(tab[x+1], 2)

        if y1 - y2 > maks:
            maks = y1 - y2

    return "".join(to_bin(maks))


file_test = open("pliki_do_zadan/DANE_M/przyklad.txt","r")
file = open("pliki_do_zadan/DANE_M/anagram.txt","r")

print(zad_3_3(file_test))
print("wynik:")
print(zad_3_3(file))