def task(n):
    a = list(set(n))
    sp = []
    count = 0
    s = []
    su = 0
    count = 1
    for i in range(len(a)): 
        s.append(a[i])
        s.append(str(n.count(a[i])))
    for i in range(0, len(s), 2):
        sp.append(s[i]+' '+s[i+1])
    print(', '.join(sp))
task(input())
