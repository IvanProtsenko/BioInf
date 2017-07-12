with open(r"C:\Новая папка\inp.txt") as inp:
    a = []
    for line in inp:
        a.append(line.strip())

    print(a[::-1])
