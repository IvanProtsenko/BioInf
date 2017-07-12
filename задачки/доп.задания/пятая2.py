def slov(d):
    d1 = {}
    kes = list(d.keys())
    for i in range(len(kes)):
        d1[d[kes[i]]] = kes[i]
    return d1
print(slov({7:'собака', 17:'я'}))
    
