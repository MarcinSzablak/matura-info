def czy_mniejszy(n, s, k1, k2):
    n -= 1
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
    tab = []

    for x in range(n):
        tab += [x+1]
    
    for x in range(n):
        for y in range(x, n):
            czy = czy_mniejszy(n, slowo, x, y)
            if czy:
                slowo[x], slowo[y] = slowo[y], slowo[x]
                tab[x], tab[y] = tab[y], tab[x]
    
    for x in range(n // 2):
        tab[x], tab[n - x - 1] = tab[n - x - 1], tab[x]

    return tab

test1 = "mascarpone"
slowo1= list(test1)
print(zad_2_3(slowo1, len(test1)))