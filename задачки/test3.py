def swap_columns(a, i, j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]
    return a

print(swap_columns([[1, 42, 68, 2, 46], [67, 98, 3, 6, 90], [6, 89, 8, 54, 27]], 2, 3))
