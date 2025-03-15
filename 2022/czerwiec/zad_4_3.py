def check_if_first(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

def zad_4_3(_file):
    for line in _file:
        l = line.strip()

        liczba = int(l)
        liczba_odwrotna = int(l[::-1])

        if check_if_first(liczba) and check_if_first(liczba_odwrotna):
            print(liczba)


file_test = open("pliki_do_zadan/przyklad.txt", "r")
file = open("pliki_do_zadan/liczby.txt", "r")

print("test:")
zad_4_3(file_test)
print("rozwiązanie")
zad_4_3(file)
