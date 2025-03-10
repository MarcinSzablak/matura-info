def czy_w(x, m, tab):
    for y in range(m):
        if tab[y] == x:
            return True
    return False

def zad_1_2(n, A):
    k = 0
    m = 0
    wystompily = []
    for x in range(n):
        if A[x] > n or czy_w(A[x], m, wystompily):
            k += 1
        wystompily += [A[x]]
        m += 1
    return k

tab1 = (1, 3, 1)
tab2 = (1, 4, 2, 5)
tab3 = (2, 2, 2, 2, 2)
print(zad_1_2(len(tab1), tab1))
print(zad_1_2(len(tab2), tab2))
print(zad_1_2(len(tab3), tab3))