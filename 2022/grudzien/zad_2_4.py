def na_binarny(n):
    binarna = []
    while n >= 1:
        binarna += [str(n % 2)]
        n = n // 2
    return "".join(binarna[::-1])

def check_czy_da_sie_dojsc(x, y):
    x_bin = na_binarny(x)
    y_bin = na_binarny(y)

    for i in range(len(x_bin)):
        if x_bin[i] != y_bin[i]:
            return False
    return True

def zad_2_4(_file):
    for line in _file:
        l = line.strip().split(" ")
        l = [int(l[0]), int(l[1])]

        if check_czy_da_sie_dojsc(l[0], l[1]):
            print(l)

file_test = open("pliki_do_zadan/pary.txt", "r")
zad_2_4(file_test)

