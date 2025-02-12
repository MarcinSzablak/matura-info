#zad 3.1
def zad_3_1(file):
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

print("zad 3.1:")
print("test 1:")
file = open("pliki_do_zadan/slowa_przyklad.txt", "r")
zad_3_1(file=file)

# rozwiązanie: 26
print("rozwiązanie 1:")
file2 = open("pliki_do_zadan/slowa.txt", "r")
zad_3_1(file=file2)


#zad 3.2
def make_word_with_pushed_letters(word):
    normal_letters = "abcdefghijklmnopqrstuvwxyz"
    pushed_letters = "nopqrstuvwxyzabcdefghijklm"

    new_word = ""

    for x in word:
        index = normal_letters.index(x)
        new_word += pushed_letters[index]
    return new_word

def zad_3_2(file):
    counter = 0
    for line in file:
        l = line.strip()
        new_word = make_word_with_pushed_letters(l)
        if l[::-1] == new_word:
            counter += 1
    file.close()
    return counter

print("zad 3.2:")
print("test 2:")
file = open("pliki_do_zadan/slowa_przyklad.txt", "r")
print(zad_3_2(file = file))

#rozwiązanie: 5
print("rozwiązanie 2:")
file = open("pliki_do_zadan/slowa.txt", "r")
print(zad_3_2(file = file))

#zad 3.3
def check_count_of_letters(word):
    set_word = set(word)
    count = []
    for x in set_word:
        count += [word.count(x)]

    for x in count:
        if x >= len(word)/2:
            return True
        else:
            return False

def zad_3_3(file):
    tab = []
    for line in file:
        l = line.strip()
        if check_count_of_letters(l):
            tab += [l]
    file.close()
    return tab


print("zad 3.3:")
print("test 3:")
file = open("pliki_do_zadan/slowa_przyklad.txt", "r")
print(zad_3_3(file = file))

# rozwiązanie:
# ['vzwzwgszezvzzlzzzzzzouz', 'azaaasfakaaaxbaaaaau', 'ppppppnoppnoclpop', 'zggggggpegpnovzgg', 'nyrpvqycpaylffffffffffffff', 'kkkkkkkkkkwpijccdbl', 'tstevttebttktnetitbttti', 'gvsvjvvvvvqppvuvcvvvi']

print("rozwiązanie 3:")
file = open("pliki_do_zadan/slowa.txt", "r")
print(zad_3_3(file = file))