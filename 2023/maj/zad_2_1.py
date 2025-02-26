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
