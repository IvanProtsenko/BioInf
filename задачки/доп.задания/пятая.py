def fun(p, p1):
    s = []
    p = list(set(p))
    p1 = list(set(p1))
    for i in range(len(p1)):
        if p1[i] in p:
            s.append(p1[i])
    return s
print(fun([1, 2, 3, 4, 5],[3, 4, 5, 6, 7, 8, 4]))
