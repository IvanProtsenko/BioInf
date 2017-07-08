def nat(n):
    h = []
    a = []
    i = n
    c = 1
    a = n.strip(' ').split(',')
    h = (''.join(a))
    print(h)
    for h in range(len(a)):
        if h[-1] % 100 == h[-1] % 1000:
            c += 1
    print(c)
nat(input())
    

