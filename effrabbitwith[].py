def fib(n):
    x = [0, 1]
    for t in range(2, n+1):
        x.append(x[t-1]+x[t-2])
    return x[-1]
print(fib(100))
