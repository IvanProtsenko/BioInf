def square(n):
    a = []
    for i in range(2*n+1):
        a.append(None)
    for i in range(2*n+1):
        if i % 2 == 0:
            a[i] = ' ---'*n+' '
        else:
            a[i] = '|   '*n+'|'
    for string in a:
        print(string)
square(int(input()))
