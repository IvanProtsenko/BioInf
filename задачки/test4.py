def angl(n):
    a = []
    g = 'aeiouy'
    s = 'bfjpvz'
    alph = 'abcdefghijklmnopqrstuvwxyz'
    a = list(n)
    for i in range(len(n)):
        if a[i] in g:
            a[i] = s[g.find(a[i])]
        elif a[i] in alph:
            a[i] = alph.find(a[i])           
    return a
print(angl(input()))
