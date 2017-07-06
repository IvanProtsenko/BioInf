def task(n):
    a = []
    b = []
    k = n.split(', ')
    for i in k:
        c = i.split(' ')
        a += [c[0]]*int(c[1])
    a.sort()
    print(', '.join(a))
    
