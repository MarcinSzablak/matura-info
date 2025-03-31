def zad_4_3(_file):
    alphabet = list("QWERTYUIOPASDFGHJKLZXCVBNM1234567890")
    password = []
    for line in _file:
        l = line.strip()

        for x in alphabet:
            new_text = x + l
            new_text_2 = l + x
            if new_text == new_text[::-1]:
                password += new_text[25]
            if new_text_2 == new_text_2[::-1]:
                password += new_text_2[25]
    print(''.join(password))

file_test = open("pliki_do_zadan/przyklad.txt", "r")
_file = open("pliki_do_zadan/napisy.txt", "r")

print("test:")
zad_4_3(file_test)

print("rozwiązanie:")
zad_4_3(_file)