def zad_4_1(_file):
    for line in _file:
        l = line.strip()
        liczba = int(l[::-1])
        if liczba % 17 == 0:
            print(liczba)

file_test = open("pliki_do_zadan/przyklad.txt", "r")
file = open("pliki_do_zadan/liczby.txt", "r")

print("test:")
zad_4_1(file_test)
print("rozwiązanie:")
zad_4_1(file)