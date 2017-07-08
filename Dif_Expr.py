import math
with open(r"C:\Users\Иванg\Downloads\norm_camp.tsv") as inp:
    first = True
    genes = []
    expr = []
    count = 0
    for line in inp:
        if first:
            caco = line.strip().split()
            b = caco.index('case')
            first = False
            continue
        l = line.strip().split()
        genes.append(l[0])
        sco = sum(map(float, l[1:b]))/(b-1)
        sca = sum(map(float, l[b:]))/(len(l)-b)
        expr.append(math.log2(sca/sco))
with open(r"C:\Users\Иванg\Desktop\gene_counts\table2.txt", 'w') as f:
    for i in range(len(expr)):
        if expr[i] > 0.1 or expr[i] < -0.1:
            f.write(genes[i]+"\n")
            count+=1
    print(count)
