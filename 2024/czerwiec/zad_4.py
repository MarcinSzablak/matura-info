
def count_no_getting(file):
    pakiety = []
    for line in file:
        l = line.strip()
        pakiety +=[int(l)]
    count = []

    for x in range(1, len(pakiety)):
        if pakiety.count(x) == 0:
            count += [x]
    print(len(count)) 

print("test 1:")
file = open("odbiorcy_przyklad.txt", "r")
count_no_getting(file)
print("rozwiązanie:")
file = open("odbiorcy.txt", "r")
count_no_getting(file)