tree = {}
heights = {}

def PGMA(d, tree):
    if len(d) == 0:
        return tree
    mini = 9999999999999999
    minis = ['', '']
    for i in d:
        for j in d[i]:
            if d[i][j] < mini:
                mini = d[i][j]
                minis[1] = i
                minis[0] = j
                for_merge = minis[1] + minis[0]
    print('Minis:{minis}'.format(minis = minis))
    dist = 0
    for key in d[minis[0]]:
        if key in minis:
            continue
        print(key)
        dist = (d[minis[0]][key] + d[minis[1]][key])/2
        if ''.join(minis) in d:
            d[''.join(minis)][key] = dist
        else:
            d[''.join(minis)] = {key: dist}
        d[key][''.join(minis)] = dist
        
    tree[''.join(minis)] = {minis[0]: 1}
    tree[''.join(minis)][minis[1]] = 1

    del d[minis[0]]
    del d[minis[1]]

    for key in d:
        if key == ''.join(minis):
            continue
        del d[key][minis[0]]
        del d[key][minis[1]]
    return PGMA(d, tree)


def ham_dist(s1, s2):
    dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            dist += 1
    return dist

with open(r'C:\Users\Иванg\Downloads\UNPHASEDconcateneted.nex') as inp:
    spisok = {}
    big_spisok = {}
    for line in inp:
        a, sequence = line.strip().split('  ')
        spisok[a] = sequence
    distance = {}
    for i in spisok:
        for i2 in spisok:
            if i == i2:
                continue
            if i not in big_spisok:
                distance[i] = {}
            if i2 not in big_spisok:
                distance[i2] = {}
            hamdist = ham_dist(spisok[i], spisok[i2])
            distance[i][i2] = hamdist
            distance[i2][i] = hamdist
                
    print(distance)

