def F(x,p, y=0):
    if x == 0:
        return [0, y+1]
    else:
        c = x % p
        if c % 2 == 1:
            result = F(x // p, p, y+1)
            return  [c + result[0], result[1]]
        else:
            result = F(x // p, p, y+1)
            return [result[0] - c, result[1]]

print("zad 2.1:")
print(F(125, 2))
print(F(130, 3))
print(F(220, 4))

def zad_2_2(p):
    maks = 0
    for x in range(0,100):
        result =F(x,p)
        if(result[0] == 0):
            maks = x
    print(maks)

print("zad 2.2")
zad_2_2(3) #96
zad_2_2(4) #97