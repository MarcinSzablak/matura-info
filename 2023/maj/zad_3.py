from numpy import empty


def zad_3_1(file):
    tab = []
    count = 0
    for line in file:
        l = line.strip()
        tab += [l]

    for x in range(len(tab)):
        if x + 1 > len(tab)-1:
            break

        y = int(tab[x] + tab[x+1])

        if y > 90:
            count += 1
    return count

file_test = open("pliki_do_zadan/pi_przyklad.txt", "r")
file = open("pliki_do_zadan/pi.txt", "r")

print("zad 3.1:")
print(zad_3_1(file_test))
print(zad_3_1(file))

def zad_3_2(file):
    tab = []

    for line in file:
        l = line.strip()
        tab += [l]

    dic = {}

    for x in range(0,100):
        dic.update({x: 0})

    for x in range(len(tab)):
        if x + 1 > len(tab) - 1:
            dic[int(tab[x])] += 1
            break

        y = int(tab[x]+ tab[x+1])

        if y in dic:
            dic[y] += 1
    maks = (0, 0)
    mini = (0, dic.get(0))

    for k, v in dic.items():
        if maks[1] < v:
            maks = (k, v)
        if mini[1] > v:
            mini = (k, v)

    return mini, maks

file_test = open("pliki_do_zadan/pi_przyklad.txt", "r")
file = open("pliki_do_zadan/pi.txt", "r")

print("zad 3.2:")
print(zad_3_2(file_test))
print(zad_3_2(file))

def zad_3_3(file):
    tab =[]
    ciagi = []
    for line in file:
        tab += [int(line.strip())]

    for x in range(len(tab)):
        if x + 5 > len(tab) - 5:
            break
        ciagi += [[tab[x],tab[x+1],tab[x+2],tab[x+3],tab[x+4],tab[x+5]]]

    count = 0
    for ciag in ciagi:
        i  = 0
        if ciag[0] < ciag[1]:
            while ciag[i] < ciag[i+1] and i < 4:
                i+=1
            while ciag[i] >= ciag[i+1] and i < 4 and ciag[i+1] != ciag[i+2]:
                i+=1
        if ciag[4] > ciag[5]:
            i+=1

        if i == 5:
            count +=1

    return count

file_test = open("pliki_do_zadan/pi_przyklad.txt", "r")
file = open("pliki_do_zadan/pi.txt", "r")

print("zad 3.3:")
print(zad_3_3(file_test))
print(zad_3_3(file))

def rosnoco_malejacy(ciag):
    i  = 0
    if ciag[0] < ciag[1]:
        while ciag[i] < ciag[i+1] and i < len(ciag) - 2:
            i+=1
        while ciag[i] >= ciag[i+1] and i < len(ciag) - 2 and ciag[i+1] != ciag[i+2]:
            i+=1
    if ciag[-2] > ciag[-1]:
        i+=1

    if i == len(ciag)-1:
        return True
    return False


def zad_3_4(file):
    maks = []
    pozycja = 0
    tab = []
    for line in file:
        tab += [int(line.strip())]

    for x in range(0,len(tab) - 1):
        for y in range(x,len(tab) - 1):
            test = tab[x:y]

            czy = False

            if len(test) > 2:
                czy = rosnoco_malejacy(test)
            if czy:
                if len(maks) < len(test):
                    maks = test
                    pozycja = x + 1
    return pozycja, maks


file_test = open("pliki_do_zadan/pi_przyklad.txt", "r")
file = open("pliki_do_zadan/pi.txt", "r")

print("zad 3.4:")
print(zad_3_4(file_test))
print(zad_3_4(file))