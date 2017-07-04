from pprint import pprint

def Score(a, b):
    if a == '-' or b == '-':
        return -1
    if a == b:
        return 1
    if a != b:
        return -1
def align(s, t):
    x = []
    for i in range(0, len(s)+1):
        r = []
        for j in range(0, len(t)+1):
            r.append(0)
        x.append(r)
    for j in range (0, len(t)+1):
        x[0][j] = 0
    for i in range (0, len(s)+1):
        x[i][0] = 0
    l = 0
    u = 0
    y = 0
    for i in range (1, len(s)+1):
        for j in range(1, len(t)+1):
            a = x[i-1][j-1] + Score(s[i-1],t[j-1])
            c = x[i-1][j] + Score(s[i-1], '-')
            d = x[i][j-1] + Score('-', t[j-1])
            if a>c and a>d and a>0:
                x[i][j] = a
            elif c>d and c>0:
                x[i][j] = c
            elif d>0: x[i][j] = d
            else: x[i][j] = 0
            
            if x[i][j]>l:
                l = x[i][j]
                u = i
                y = j
    i = u
    j = y
    sa = ""
    ta = ""

    while (x[i][j] != 0):
        if i>0 and j>0 and x[i-1][j-1] + Score(s[i-1],t[j-1]) == x[i][j]:
            sa = s[i-1] + sa
            ta = t[j-1] + ta
            i -= 1
            j -= 1
        if i>0 and x[i][j] == x[i-1][j] + Score(s[i-1], '-'):
            sa = s[i-1] + sa
            ta = '-' + ta
            i -= 1
        if j>0 and x[i][j] == x[i][j-1] + Score('-', t[j-1]):
            ta = t[j-1] + ta
            sa = '-' + sa
            j -= 1
            
    print (sa)
    print (ta)
    
    pprint(x)
