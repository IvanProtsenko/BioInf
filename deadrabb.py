def fibb(n):
    h = [1, 1]
    for k in range(2, n + 1):
        h.append(h[k-1]+h[k-2])

    return h

def fib(n, m):
    x = fibb(m)
    print(x)
    for t in range(m + 1, n + 1):
        x.append(x[t-1]+x[t-2]-x[t-m-1])
    print(x)
                 
    return x[n]                


for i in range(7):
    print(fib(i, 3))


