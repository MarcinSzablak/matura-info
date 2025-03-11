def zad_4_1(_file):
    counter = 0
    first = 0
    for line in _file:
        l = list(line.strip())
        if l[0] == l[-1]:
            counter += 1
            if first == 0:
                first = int(''.join(l))
    return counter, first

file_test = open("pliki_do_zadan/przyklad.txt", "r")
file = open("pliki_do_zadan/liczby.txt", "r")

print(zad_4_1(file_test))
print(zad_4_1(file))