def task(n):
    a = 0
    s = 0
    for a in range(n):
        if a % 5==0:
            s += a
        elif a % 3==0:
            s += a
    return s
    
    
