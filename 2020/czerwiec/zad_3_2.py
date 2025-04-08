def zad_3_2(n):
    w = 0
    while n != 0:
        w += n % 10
        print(w, end=" ")
        n //= 10
    print("")
    return w

print(zad_3_2(45778))
print(zad_3_2(1234))
print(zad_3_2(11111))