def Algo(n):
    counter = 0
    if n <= 2:
        return 1, counter
    else:
        p = 1
        k = n
        while k - p > 1:
            s = (p + k) // 2
            counter += 1
            if s * s <= n:
                p = s
            else:
                k = s
        return p, counter

print(Algo(5))
print(Algo(2))
print(Algo(64))
print(Algo(1024))