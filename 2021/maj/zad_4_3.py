def zad_4_3(_file):
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    counter = dict()

    for x in range(0, len(alphabet)):
        couter = counter.update({alphabet[x]: 0})

    for line in _file:
        l = line.strip().split()
        
        komenda = l[0]
        litera = l[1]

        if komenda == "DOPISZ":
            counter[litera] += 1

    maks_value = 0
    for v in counter.values():
        if maks_value < v:
            maks_value = v

    return maks_value

        
file_test = open("pliki_do_zadan/przyklad.txt", "r")
file = open("pliki_do_zadan/instrukcje.txt", "r")

wynik_test = zad_4_3(file_test)
wynik = zad_4_3(file)

print(wynik_test)
print(wynik)