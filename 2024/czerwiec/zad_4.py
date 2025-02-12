#zad 4.2
def count_no_getting(file):
    pakiety = []
    for line in file:
        l = line.strip()
        pakiety +=[int(l)]
    count = []

    for x in range(1, len(pakiety)):
        if pakiety.count(x) == 0:
            count += [x]
    print(len(count))

print("zad 4.2:")

test_file = open("pliki_do_zadan/odbiorcy_przyklad.txt", "r")
file = open("pliki_do_zadan/odbiorcy.txt", "r")

print("test:")
count_no_getting(test_file)
print("rozwiązanie:")
count_no_getting(file)

#zad 4.3
def runda(komputery, pakiety):
    komputery_kopia = list(komputery)
    for i in range(len(pakiety)):
        komputery[i] = komputery_kopia[pakiety[i] - 1]
    return komputery

def check_fastest_return(file):
    pakiety = []
    for line in file:
        l = line.strip()
        pakiety += [int(l)]

    komputery = list(range(1, len(pakiety)+1))

    r = 0

    while True:
        pomoc = runda(komputery, pakiety)
        r += 1
        for i in range(len(pomoc)):
            if pomoc[i] == i+1:
                return [r, i+1]

print("zad 4.3:")

test_file = open("pliki_do_zadan/odbiorcy_przyklad.txt", "r")
file = open("pliki_do_zadan/odbiorcy.txt", "r")

print("test:")
print(check_fastest_return(test_file))
print("rozwiązanie:")
print(check_fastest_return(file))

#zad 4.4
def check_overload(file):
    pakiety = []
    for line in file:
        l = line.strip()
        pakiety +=[int(l)]

    komputery = list(range(1, len(pakiety)+1))

    for i in range(8):
        pomoc = runda(komputery, pakiety)
        if i in [0,1,3,7]:
            max = 0
            set_pomoc = set(pomoc)
            for x in set_pomoc:
                if pomoc.count(x) > max:
                    max = pomoc.count(x)

            #print(pomoc)
            print(max , " ", end="")
    print("")


print("zad 4.4:")

test_file = open("pliki_do_zadan/odbiorcy_przyklad.txt", "r")
file = open("pliki_do_zadan/odbiorcy.txt", "r")

print("test: ")
check_overload(test_file)
print("rozwiązanie: ")
check_overload(file)