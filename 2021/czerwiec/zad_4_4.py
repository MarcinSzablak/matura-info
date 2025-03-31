def zad_4_4(_file):
    numery = list("1234567890")
    password = []
    count_x = 0
    for line in _file:
        l = line.strip()

        for x in range(0, len(l),2):
            if count_x == 3:
                break
            if l[x] in numery and l[x+1] in numery:
                liczba = int(str(l[x] + l[x+1]))
                if liczba >= 65 and liczba <= 90:
                    password += chr(liczba)
                    if chr(liczba) == "X":
                        count_x += 1
    print("".join(password))

file_test = open("pliki_do_zadan/przyklad.txt", "r")
_file = open("pliki_do_zadan/napisy.txt", "r")


print("test:")
zad_4_4(file_test)

print("rozwiązanie:")
zad_4_4(_file)