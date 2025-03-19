def zad_3_4(_file):
    tab_hex = []
    for line in _file:
        l = int(line.strip())

        
        tab_hex += [(hex(l)[2:]).upper()]

    maks = max(tab_hex)

    dict_hex = dict()
    for x in range(0, 16):
        dict_hex.update({(hex(x)[2:]).upper(): 0})

    for key in dict_hex.keys():
        counter = 0

        tab_pomoc = tab_hex

        for x in range(len(tab_pomoc)):
            for y in range(0, len(tab_pomoc[x])):
                if tab_pomoc[x][y] in key:
                    counter += 1
        dict_hex[key] = counter
    
    return dict_hex

file_test = open("pliki_do_zadan/liczby_przyklad.txt", "r")
file = open("pliki_do_zadan/liczby.txt", "r")

print("test: ", zad_3_4(file_test))

print("rozwiązanie: ", zad_3_4(file))