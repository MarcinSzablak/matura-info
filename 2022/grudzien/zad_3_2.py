# def sito(n):
#     tab = [False, False]
#     for x in range(2, n):
#         tab += [True]
#     for x in range(2, int(n**0.5)+1):
#         for y in range(x, n):
#             if y % x == 0:
#                 tab[y] = False
#     return tab

def check_if_pierwsza(n):
    for x in range(2, int(n**0.5)+ 1):
        if n % x == 0:
            return False
    return True

def zad_3_2(_file):
    counter = 0
    for line in _file:
        l = int(line.strip())
        liczba = l - 1
        
        if check_if_pierwsza(liczba):
            counter += 1
    return counter

file_test = open("pliki_do_zadan/liczby_przyklad.txt", "r")
file = open("pliki_do_zadan/liczby.txt", "r")

print("test: ", zad_3_2(file_test))

print("rozwiązanie: ", zad_3_2(file))