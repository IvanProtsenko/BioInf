flagok_n=0
left_n=0
right_n=0
flagok_h=0
left_h=0
right_h=0
name_gene=[]
stplus = []
stminus = []

with open (r"C:\Users\Иванg\Desktop\gene_counts\genome_annotation.gtf") as imp:
    for line in imp:
        gene_info=line.strip().split('\t') 
        name_gene.append(line.strip().split('"')[5])
        if gene_info[6] == '+':
            stplus.append([int(gene_info[3]), int(gene_info[4]), gene_info[6], line.strip().split('"')[5], 0, 0])
        if gene_info[6] == '-':
            stminus.append([int(gene_info[3]), int(gene_info[4]), (gene_info[6]), line.strip().split('"')[5], 0, 0])
            
def count_reads(filename, idx):
    with open (filename) as imp:
        t_genp=0
        t_genm=0
        for line in imp:
            if line[0] == "@":
                continue
            gene_info=line.strip().split('\t')
            flagok_n=int(gene_info[1])
            left_n=int(gene_info[3])
            right_n=left_n+len(gene_info[9])
            
            if flagok_n&4:
                continue
            if flagok_n&16:  
                while t_genm<len(stminus):
                    if right_n<stminus[t_genm][0]:
                        break
                    elif left_n <= stminus[t_genm][1]:
                        stminus[t_genm][idx] += 1
                        break
                    else:
                        t_genm += 1
            else:
                while t_genp<len(stplus):
                    if right_n<stplus[t_genp][0]:
                        break
                    elif left_n < stplus[t_genp][1] and right_n > stplus[t_genp][0]:
                        stplus[t_genp][idx] += 1
                        break
                    else:
                        t_genp += 1


count_reads(r"C:\Users\Иванg\Desktop\gene_counts\THYP2_22.sam", 4)
count_reads(r"C:\Users\Иванg\Desktop\gene_counts\TNOR2_22.sam", 5)

print("gene\t thyp\t nor")
with open(r"C:\Users\Иванg\Desktop\gene_counts\table.txt", 'w') as f:
    for gene in stplus:
        print(gene[3], gene[4], gene[5], sep='\t', file=f)
    for gene in stminus:
        print(gene[3], gene[4], gene[5], sep='\t', file=f)                
                    
                    
                              

                

        





