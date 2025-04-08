def czy_k_podobne(n, A, B):
    k = 0
    while k < n:

        for i in range(1, k+1):
            if B[n - k + i - 1] == A[i - 1]:
                return True

        for i in range(1, n - k + 1):
            if B[i - 1] == A[k + i - 1]:
                return True

        k += 1

    return False

a = [9, 8, 7, 6, 0]
b = [3, 4, 5, 1, 2]
n = 5
print(czy_k_podobne(n, a, b))