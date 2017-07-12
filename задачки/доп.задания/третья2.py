def square(n):
    s = []
    for i in range(n):
        s.append([])
    for i in range(n):
        for j in range(n): 
            s[i].append(0)
    a = list(range(n))
    g = a[:]
    for i in a:
        if is_prime(i):
            s[1][i] = 1
            s[i][1] = 1
    return s

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and n // i != 1:
            return False
    if n<2:
        return False
    return True
print(square(int(input())))
