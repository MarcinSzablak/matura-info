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

    return tab[0]

def zad_2_4(file):
    for line in file:
        l = line.strip().split()
        n  = int(l[0])
        slowo = list(l[1])
        slowo_copy = list(l[1])

        index = zad_2_3(slowo_copy, n)

        #print(index)
        print("".join(slowo[index-1:]))


file_test = open("pliki_do_zadan/DANE_M/sufiks_4.txt","r")
file = open("pliki_do_zadan/DANE_M/slowa4.txt","r")
zad_2_4(file_test)
print("wyniki:")
zad_2_4(file)