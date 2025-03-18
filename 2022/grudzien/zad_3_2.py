# def sito(n):
#     tab = [False, False]
#     for x in range(2, n):
#         tab += [True]

#     for x in range(2, int(n**0.5)+1):
#         for y in range(x, n):
#             if y % x == 0:
#                 tab[y] = False
#     return tab

def zad_3_2(_file):
    for line in _file:
        l = int(line.strip())
        liczba = l - 1

print(sito(12))