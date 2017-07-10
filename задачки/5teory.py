def one(n):
    a = []
    j = 0
    for i in range(n):
        a.append([])
    for i in range(n):
        for j in range(n):
            if i == j:
                a[i].append(1)
            else:
                a[i].append(0)
    return a
print(one(int(input())))
            
        
    
