def func(n, a):
    s = []
    for i in range(n):
        s.append(a[i][:-n])
    s[-1] = a[-1]
    s[0] = a[0][:-n]
    return s
    
print(''.join(func(3, ['', '', ''])))
