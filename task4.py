def task(n):
    a = []
    k = n.split(' ')
    for i in k:
        if i not in a:
            a.append(i)
    print(a)
    
