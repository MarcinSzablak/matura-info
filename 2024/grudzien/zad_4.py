from xml.dom.expatbuilder import theDOMImplementation


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
            mini = a*b
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

    counter = 0
    save_array = []
    help_array = []
    maks = 0
    for x in range((len(tab))):
        if x >= len(tab) - 1:
            break
        if tab[x][0] >= tab[x+1][0] and tab[x][1] >= tab[x+1][1]:
            counter += 1
            help_array += [tab[x]]
        else:
            if maks <= counter:
                maks = counter + 1
                save_array = help_array
                save_array += [tab[x]]
            counter = 0
            help_array = []

    return maks, save_array[-1]

file_test = open("pliki_do_zadan/prostokaty_przyklad.txt", "r")
file = open("pliki_do_zadan/prostokaty.txt", "r")

print("zad 4.2:")
print(zad_4_2(file_test))
print(zad_4_2(file))

def zad_4_3(_file):
    tab = []
    for line in _file:
        l = line.strip().split()
        a = int(l[0])
        b = int(l[1])
        tab += [[a, b]]

    tab.sort(reverse = True)

    two_ractangles = 0
    three_ractangles = 0
    five_ractangles = 0

    for x in range(len(tab)):
        if x >= len(tab) - 1:
            break
        if tab[x][0] == tab[x+1][0] and two_ractangles < tab[x][1] + tab[x+1][1]:
                two_ractangles = tab[x][1] + tab[x+1][1]
    for x in range(len(tab)):
        if x >= len(tab) - 1:
            break
        if tab[x][0] == tab[x+1][0] == tab[x+2][0] and three_ractangles < tab[x][1] + tab[x+1][1] + tab[x+2][1]:
            three_ractangles = tab[x][1] + tab[x+1][1] + tab[x+2][1]
    for x in range(len(tab)):
        if x >= len(tab) - 1:
            break
        if tab[x][0] == tab[x+1][0] == tab[x+2][0] == tab[x+3][0] == tab[x+4][0] and five_ractangles < tab[x][1] + tab[x+1][1] + tab[x+2][1] + tab[x+3][1] + tab[x+4][1]:
            five_ractangles = tab[x][1] + tab[x+1][1] + tab[x+2][1] + tab[x+3][1] + tab[x+4][1]


    return two_ractangles, three_ractangles, five_ractangles

file_test = open("pliki_do_zadan/prostokaty_przyklad.txt", "r")
file = open("pliki_do_zadan/prostokaty.txt", "r")

print("zad 4.3:")
print(zad_4_3(file_test))
print(zad_4_3(file))