#zad 3.1
def read_file(file):
    counter = 0

    for line in file:
        i = 0
        l = line.strip()
        while len(l) != i:
            if l[i] == "k" and i <= len(l)-3 and l[i+2] == "t":
                counter += 1
            i += 1

    print(counter)
    file.close()

file = open("slowa_przyklad.txt", "r")
read_file(file=file)

# rozwiązanie 26
file2 = open("slowa.txt", "r")
read_file(file=file2)
