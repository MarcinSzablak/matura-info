def zad_3_1(file):
    zrownowazone = 0
    prawie_zrownowazone = 0
    for line in file:
        l = line.strip()
        jeden = l.count("1")
        zero = l.count("0")

        if jeden == zero:
            zrownowazone += 1
        elif jeden - zero == 1 or zero - jeden == 1:
            prawie_zrownowazone += 1
    print(zrownowazone)
    print(prawie_zrownowazone)

file_test = open("pliki_do_zadan/DANE_M/przyklad.txt","r")
file = open("pliki_do_zadan/DANE_M/anagram.txt","r")

zad_3_1(file_test)
print("wyniki: ")
zad_3_1(file)