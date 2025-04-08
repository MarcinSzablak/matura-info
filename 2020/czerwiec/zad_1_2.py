def czy_k_podobne(n, A, B, k):
    for i in range(1, k+1):
        if B[n - k + i - 1] != A[i - 1]:
            return False

    for i in range(1, n - k + 1):
        if B[i - 1] != A[k + i - 1]:
            return False

    return True

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 1, 2]
n = 5
k = 2
print(czy_k_podobne(n, a, b, k))

a = [1,1,1,1,3,1,1,1,1]
b = [3,1,1,1,1,1,1,1,1]
n = 9
k = 4
print(czy_k_podobne(n, a, b, k))

a = [4, 2, 4, 4, 2, 6]
b = [4, 4, 2, 6, 4, 2]
n = 6
k = 1
print(czy_k_podobne(n, a, b, k))