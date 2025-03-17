def zad_1_1(tab):
    counter = 0
    for x in range(1, len(tab) - 1):
        if tab[x - 1] != tab[x]:
            counter += 1
    return counter

print("test:")

file_test = open("pliki_do_zadan/mecz_przyklad.txt", "r")
mecz_test = list(file_test.readline())
print(zad_1_1(mecz_test))

print("rozwiązanie: ")

file = open("pliki_do_zadan/mecz.txt", "r")
mecz = list(file.readline())
print(zad_1_1(mecz))