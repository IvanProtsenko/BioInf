def text(n):
    s = ''
    a = n.split()
    a.sort()
    c = 1
    g = 0
    print(a)
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            c += 1    
        else:
            if c>g:
                s = a[i-1]
                g = c
            c = 1
    print(s)
text(input())
