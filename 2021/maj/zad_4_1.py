def zad_4_1(_file):
    alfabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    przesuniencie = list('BCDEFGHIJKLMNOPQRSTUVWXYZA')

    ciong = []

    for line in _file:
        l = line.strip().split(" ")
        komenda = l[0]
        litera = l[1]

        if komenda == "DOPISZ":
            ciong += [litera]
        elif komenda == "ZMIEN":
            ciong[-1] = litera
        elif komenda == "USUN":
            ciong.pop()
        elif komenda == "PRZESUN":
            for x in range(0, len(ciong)):
                if ciong[x] == litera:
                    index = alfabet.index(litera)
                    ciong[x] = przesuniencie[index]
                    break
    return "".join(ciong)

file_test = open("pliki_do_zadan/przyklad.txt", "r")
file = open("pliki_do_zadan/instrukcje.txt", "r")

wynik_test = zad_4_1(file_test)
wynik = zad_4_1(file)


# jest to rozwiązanie do zad 4.4
print(wynik_test)
print(wynik)

print(len(wynik_test)) #10
print(len(wynik)) #517

