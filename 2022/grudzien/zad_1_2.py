def zad_1_2(tab):
    A = 0
    B = 0
    for x in range(0, len(tab)):
        if tab[x] == "A":
            A += 1
        else:
            B += 1

        if A >= 1000 and A - B >= 4:
            print(A, ":", B , "A")
            A = B = 0
        elif B >= 1000 and B - A >= 4:
            print(A, ":", B, "B")
            A = B = 0

print("test:")

file_test = open("pliki_do_zadan/mecz_przyklad.txt", "r")
mecz_test = list(file_test.readline())
zad_1_2(mecz_test)

print("rozwiązanie: ")

file = open("pliki_do_zadan/mecz.txt", "r")
mecz = list(file.readline())
zad_1_2(mecz)