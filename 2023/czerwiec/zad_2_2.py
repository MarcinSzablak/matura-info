def czy_mniejszy(n, s, k1, k2):
    i = k1
    j = k2
    while  i <= n and j <= n:
        if (s[i] == s[j]):
            i += 1
            j += 1
        else:
            if(s[i] < s[j]):
                return "TAK"
            else:
                return "NIE"
    if j <= n:
        return "TAK"
    else:
        return "NIE"
            
def zad_2_2(file):
    n = int(file.readline().strip()) - 1
    s = file.readline().strip() 
    k = file.readline().strip().split()
    k1 = int(k[0])
    k2 = int(k[1]) 

    print(czy_mniejszy(n, s, k1, k2))

test_file_1 = open("pliki_do_zadan/DANE_M/sufiks_1.txt", "r")
test_file_2 = open("pliki_do_zadan/DANE_M/sufiks_2.txt", "r")

file_1 = open("pliki_do_zadan/DANE_M/slowa1.txt", "r")
file_2 = open("pliki_do_zadan/DANE_M/slowa2.txt", "r")
file_3 = open("pliki_do_zadan/DANE_M/slowa3.txt", "r")

zad_2_2(test_file_1)
zad_2_2(test_file_2)
print("wyniki: ")
zad_2_2(file_1)
zad_2_2(file_2)
zad_2_2(file_3)