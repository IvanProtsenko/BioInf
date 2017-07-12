def func(n):
    spy = []
    for i in range(1, len(n)//2 + 1):
        spy.append((n[i-1], n[-i]))
    return spy
print(func([1,2,3,4,5,6]))
    
