with open(r"input.txt") as inp:
    a = 0
    for line in inp:
        line = line.strip().split()
        if int(line[1])>a:
            a = int(line[1])
