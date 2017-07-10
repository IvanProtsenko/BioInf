def text(n):
    dif_w = list(set(n))
    s = ''
    n.sort()
    c = 1
    g = 0
    for word in dif_w:
        c = n.count(word)
        if c>g:
            g = c
            s = word
    return s
#text(input())

def consensus(string_list):
    r = []
    res = []
    for i in range(len(string_list[0])):
        r.append([])
        for j in range(len(string_list)):
            r[i].append('')
    for i in range(len(string_list)):
        for j in range(len(string_list[0])):
            r[j][i] = string_list[i][j]
    for string in r:
        res.append(text(string))
    return ''.join(res)
y = input()
arr = []
while y != '0':
    arr.append(list(y))
    y = input()
print(consensus(arr))
            
    



    
