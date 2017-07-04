def fib(c):
    n = 1;
    t = 1;
    for i in range(c):
        h=n+t
        n=t;
        t=h;
    return t
    
