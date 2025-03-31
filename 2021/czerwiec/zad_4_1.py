def zad_4_1(_file):
    count = 0
    liczby = list("1234567890")
    for line in _file:
        l = line.strip()

        for x in l:
            if x in liczby:
                count += 1
    print(count)

file_test = open("pliki_do_zadan/przyklad.txt", "r")
_file = open("pliki_do_zadan/napisy.txt", "r")


print("test:")
zad_4_1(file_test)

print("rozwiązanie:")
zad_4_1(_file)