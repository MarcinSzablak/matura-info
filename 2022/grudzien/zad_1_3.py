def zad_1_3(tab):
    passy = 0
    A = 0 
    B = 0

    maks = (0, "")
    
    for i in range(0, len(tab) - 1):
        if i == len(tab) - 2 and tab[i] == 'A' and tab[i] == tab[i + 1]:
            A += 1
        elif i == len(tab) - 2 and tab[i] == 'B' and tab[i] == tab[i + 1]:
            B += 1 

        if tab[i] == tab[i + 1] and tab[i] == 'A':
            A += 1 
        elif tab[i] == tab[i + 1] and tab[i] == 'B':
            B += 1

        else:
            if A >= 10 or B >= 10:
                passy += 1

            if maks[0] < A:
                maks = (A, "A")
            elif maks[0] < B:
                maks = (B, "B")

            A = 0
            B = 0

    return passy, maks



print("test:")

file_test = open("pliki_do_zadan/mecz_przyklad.txt", "r")
mecz_test = list(file_test.readline())
print(zad_1_3(mecz_test))

print("rozwiązanie: ")

file = open("pliki_do_zadan/mecz.txt", "r")
mecz = list(file.readline())
print(zad_1_3(mecz))