def zad_2(n):
    COUNTER = 0
    a = 0
    b = 1
    c = 0
    while n > 0:
        a = n % 10
        n = n // 10
        if a % 2 == 0:
            c = c + b * a // 2
        else:
            COUNTER += 1
            c = c + b
        b = b * 10
    return [COUNTER,b,c]

print("zad 2.1:")
print(zad_2(33658))
print(zad_2(542102))
print(zad_2(87654321012345678))

print("zad 2.2:")
print(zad_2(333333666666999999))