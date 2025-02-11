#more code but no reverse needee
def to_binary(n):
    if n == 0:
        return [0]

    x = 1
    binary = []

    while x <= n:
        x *= 2
    x //= 2

    while x >= 1:
        if n >= x:
            binary.append(1)
            n -= x
        else:
            binary.append(0)
        x //= 2

    return binary


#less code but you need to reverse array
def to_binary_with_reverse(n):
    if n == 0:
        return [0]

    binary = []

    while n > 0:
        binary += [n % 2]
        n = n // 2

    return binary[::-1]

def check_last_index(k,w,n):
    binary = to_binary(n)
    index = (k*w) - 1

    while len(binary) - 1 < index:
        binary += binary

    return binary[index]


print("test 1:")
print(check_last_index(k = 3, w = 5, n = 19))
print("test 2:")
print(check_last_index(k = 5, w = 4, n = 179))