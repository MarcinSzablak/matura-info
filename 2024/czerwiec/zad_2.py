#zad 2.1
def F(x, y = 0):
    if x == 0:
        return [0 , y + 1]
    else:
        result = F(x//2, y+1)
        return [2 + result[0] , result[1]]


print("zad 2.1:")
print("test 1:")
print(F(3))
print("test 2:")
print(F(16))
print("test 3:")
print(F(35))


#zad 2.2
def find():
    tab = []

    for x in range(35, 1000):
        tab += [x]

    tab1= []

    for x in range(0, len(tab)):
        test = F(tab[x])
        if test[0] == 18:
            tab1 += [tab[x]]

    print(tab1)

print("zad 2.2:")
find()

#min = 256
#max = 511
