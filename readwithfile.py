from pprint import pprint

def Score(a, b):
    if a == '-' or b == '-':
        return -1
    if a == b:
        return 1
    if a != b:
        return -1
def align(s, t):
    x = []
    for i in range(0, len(s)+1):
        r = []
        for j in range(0, len(t)+1):
            r.append(0)
        x.append(r)
    for j in range (0, len(t)+1):
        x[0][j] = 0
    for i in range (0, len(s)+1):
        x[i][0] = 0
    l = 0
    u = 0
    y = 0
    for i in range (1, len(s)+1):
        for j in range(1, len(t)+1):
            a = x[i-1][j-1] + Score(s[i-1],t[j-1])
            c = x[i-1][j] + Score(s[i-1], '-')
            d = x[i][j-1] + Score('-', t[j-1])
            if a>c and a>d and a>0:
                x[i][j] = a
            elif c>d and c>0:
                x[i][j] = c
            elif d>0: x[i][j] = d
            else: x[i][j] = 0         
            if x[i][j]>l:
                l = x[i][j]
                u = i
                y = j
    i = u
    j = y
    sa = ""
    ta = ""
    while (x[i][j] != 0):
        if i>0 and j>0 and x[i-1][j-1] + Score(s[i-1],t[j-1]) == x[i][j]:
            sa = s[i-1] + sa
            ta = t[j-1] + ta
            i -= 1
            j -= 1
        if i>0 and x[i][j] == x[i-1][j] + Score(s[i-1], '-'):
            sa = s[i-1] + sa
            ta = '-' + ta
            i -= 1
        if j>0 and x[i][j] == x[i][j-1] + Score('-', t[j-1]):
            ta = t[j-1] + ta
            sa = '-' + sa
            j -= 1           
    print (sa)
    print (ta)
    print('\n')
    return i  
    #pprint(x)

with open(r"C:\Users\Иванg\Downloads\small_ref.fa") as inp:
    first = True
    ref = ""
    ref_name = ""
    for line in inp:
        if first:
            ref_name=line.strip()
            first = False
            continue
        ref += line.strip()
print(ref)
print(ref_name)

with open(r"C:\Users\Иванg\Downloads\output.txt", 'w') as out:
    with open(r"C:\Users\Иванg\Downloads\small.fastq", 'r') as inp:
        counter = 1
        read_name = ''
        read = ''
        read_quality = ''
        for line in inp:
            if counter == 1:
                read_name = line.strip()
                counter += 1
                continue
            if counter == 2:
                read = line.strip()
                counter += 1
                continue
            if counter == 3:
                counter += 1
                continue
            if counter == 4:
                counter = 1
                read_quality = line.strip()
                res = align(ref, read)
            print(read_name, ref_name, res, read, read_quality, sep='\t', file=out)
        for line in inp: 
            l=line.strip()
    
