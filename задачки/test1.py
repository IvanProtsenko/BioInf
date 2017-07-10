def nat(n):
    g = 0
    c = 1
    a = n
    print(a)
    for h in range(1, len(a)):
        if a[h-1] == a[h]:
            c += 1
        elif c>g:
            g = c
            c = 1
        else:
            c = 1
    print(g)
nat(list(map(int, input().split(','))))
    

