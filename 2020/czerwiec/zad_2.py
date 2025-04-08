def sym(a, b):
    if a != 0:
        sym(a - 1, b + 1)
        print(a*b, end = " ")
        sym(a- 1, b + 1)


sym(3, 1)
print("")
sym(4, 2)
print("")
sym(3, 3)
print("")
sym(4, 1)

def sym2(a, b, tab):
    if a != 0:
        sym2(a - 1, b + 1, tab)
        tab += [a*b]
        sym2(a- 1, b + 1, tab)


print("\nzad 2.2:")
tab = []
sym2(5, 1, tab)
print(len(tab))

tab = []
sym2(6, 6, tab)
print(len(tab))

tab = []
sym2(10, 2020, tab)
print(len(tab))