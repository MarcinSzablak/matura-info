def zad_2_1(x):
    if x == 0:
        return 1

    z = 0
    c = 0
    counter = 0

    while x > 0:
        p = x % 2
        if p == z:
            c += 1
        else:
            c = 0
            counter += 1
        x //= 2
        z = p

    return counter

print("zad_2_1:")
print(zad_2_1(67))
print(zad_2_1(245))


def zad_2_2(file):
    counter = 0
    for line in file:
        l = line.strip()

        c = 1

        for x in range(len(l)-1, -1, -1):
            if len(l) == 1:
                counter += 1
                break

            if x == 0:
                if l[x] != l[x+1]:
                    c+=1
                break

            if l[x] != l[x-1]:
                c+=1
        if c <= 2:
            counter += 1

    return counter


file_test = open("pliki_do_zadan/bin_przyklad.txt", "r")
file = open("pliki_do_zadan/bin.txt", "r")

print("zad_2_2:")
print(zad_2_2(file_test))
print(zad_2_2(file))

def zad_2_3(file):
    tab = []
    for line in file:
        l = int(line.strip())
        tab += [l]
    tab.sort()
    return tab[-1]

file_test = open("pliki_do_zadan/bin_przyklad.txt", "r")
file = open("pliki_do_zadan/bin.txt", "r")

print("zad_2_3:")
print(zad_2_3(file_test))
print(zad_2_3(file))


print("zad_2_4:")
print(bin(123))
print(bin(int("2D", 16)))

'''
1111011 - > 123
0101101
-------
1010110 - > (123 XOR 101101)
0101101 -> XOR 2D
-------
1111011 -> 123
'''

def zad_2_5(file):
    for line in file:
        p = int(line.strip(),2)
        c = int(p / 2)
        pb = list(bin(p))[2:]
        cb = list(bin(c))[2:]

        while len(cb) != len(pb):
            cb.insert(0,'0')

        new = []
        for x in range(len(pb)):
            if pb[x] != cb[x]:
                new += ["1"]
            else:
                new += ["0"]

        print(''.join(new))


print("zad_2_5:")
file_test = open("pliki_do_zadan/bin_przyklad.txt", "r")
file = open("pliki_do_zadan/bin.txt", "r")

#zad_2_5(file_test)
zad_2_5(file)
