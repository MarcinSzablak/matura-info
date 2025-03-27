def szukanie_zachlanne_suma_kwadratow(n):
    s = 0
    kw = 1
    while kw * kw < n:
        kw += 1

    if kw * kw > n:
        kw = kw - 1
    s = n - kw * kw
    dl = 1

    while s > 0:
        if kw*kw < s:
            s = s - kw*kw
            dl += 1
            if kw == 0:
                break
        else:
            kw -= 1
    print(dl)

szukanie_zachlanne_suma_kwadratow(23)