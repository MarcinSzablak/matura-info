def czy_mniejszy(n, s, k1, k2):
    i = k1
    j = k2
    while  i <= n and j <= n:
        if (s[i] == s[j]):
            i += 1
            j += 1
        else:
            if(s[i] < s[j]):
                return True
            else:
                return False
    if j <= n:
        return True
    else:
        return False

def zad_2_3(slowo, n):
    tab = [0] * n

    miejsce = 0

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if czy_mniejszy(n - 1 , slowo, i, j) == False:
                miejsce += 1
        tab[miejsce] = i + 1
        miejsce = 0

    return tab

test1 = "mascarpone"
slowo1 = list(test1)
test2 = "kalafiorowa"
slowo2 = list(test2)

print(zad_2_3(slowo1, len(test1)),slowo1)
print(zad_2_3(slowo2, len(test2)),slowo2)
