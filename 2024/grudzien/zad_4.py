def zad_4_1(_file):
    mini = 0
    maks = 0

    for line in _file:
        l = line.strip().split()
        a = int(l[0])
        b = int(l[1])

        if maks < a*b:
            maks = a*b

        if mini == 0:
            mini = maks
        elif mini > a*b:
            mini = a*b

    return mini,maks

file_test = open("pliki_do_zadan/prostokaty_przyklad.txt", "r")
file = open("pliki_do_zadan/prostokaty.txt", "r")

print("zad 4.1:")
print(zad_4_1(file_test))
print(zad_4_1(file))

def zad_4_2(_file):
    tab = []
    for line in _file:
        l = line.strip().split()
        a = int(l[0])
        b = int(l[1])
        tab += [[a,b]]

    last_ractangle = [tab[0]]

    for i in range(1, len(tab)):
        if tab[i][0] < last_ractangle[-1][0] and tab[i][1] < last_ractangle[-1][1]:
            last_ractangle.append(tab[i])

    return last_ractangle

file_test = open("pliki_do_zadan/prostokaty_przyklad.txt", "r")
file = open("pliki_do_zadan/prostokaty.txt", "r")

print("zad 4.2:")
print(zad_4_2(file_test))
#print(zad_4_2(file))
