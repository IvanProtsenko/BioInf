def dump_graph(outgoing, viz_fname):
    with open(viz_fname, 'w') as out_f:
        print('digraph ag{', file=out_f)
        for left, dict in outgoing.items():
            for right in dict:
                round_coverage = dict[right][0]
                print(left + '[label="{}"]'.format(left), file=out_f)
                print(right + '[label="{}"]'.format(right), file=out_f)
                print(
                    left + ' -> ' + right +
                    '[label="C = {}"]'.format(round_coverage),
                    file=out_f)
        print('}', file=out_f)

x = [1, 0, 3, 7, -5, 30, 61, 17, 42]
visited = []
for i in range(len(x)):
    visited.append(False)
stack = [0]
listik = {0:[4, 8], 8:[0, 2], 4:[0, 2], 2:[3, 4, 5, 8], 3:[2], 5:[2, 7], 7:[1, 5], 1:[7]}
maxik = min(x)-1
while stack:
    cur_v = stack.pop()
    visited[cur_v] = True
    for neig in listik[cur_v]:
        if not visited[neig] and neig not in stack:
            stack.append(neig)
    if x[cur_v]>maxik:
        maxik = x[cur_v]
        maxv = cur_v

from collections import deque
x = [1, 0, 3, 7, -5, 30, 61, 17, 42]
visited = []
for i in range(len(x)):
    visited.append(False)
queue = deque()
queue.append(0)
listik = {0:[4, 8], 8:[0, 2], 4:[0, 2], 2:[3, 4, 5, 8], 3:[2], 5:[2, 7], 7:[1, 5], 1:[7]}
maxik = min(x)-1
while queue:
    cur_v = queue.popleft()
    visited[cur_v] = True
    for neig in listik[cur_v]:
        if not visited[neig] and neig not in queue:
            queue.append(neig)
    if x[cur_v]>maxik:
        maxik = x[cur_v]
        maxv = cur_v

def extract_Kmers(read, K):
    xf = []
    for i in range(len(read)-K+1):
        xf.append(read[i:K+i])
    return xf

def Create_graph_out(xf, slov, key):
    for i in range(len(xf)-1):
        if xf[i] not in slov:
            slov[xf[i]] = {}
        if xf[i+1] not in slov[xf[i]]:
            slov[xf[i]][xf[i+1]] = [0, xf[i]+xf[i+1][key - 1:]]
        slov[xf[i]][xf[i+1]][0] += 1
    return slov
#print(Create_graph(extract_Kmers('GACTGTA', 4), {'GACT':{'ACTG': 2}}))

def Create_graph_in(xf, slov1, key):
    for i in range(len(xf)-1):
        if xf[i+1] not in slov1:
            slov1[xf[i+1]] = {}
        if xf[i] not in slov1[xf[i+1]]:
            slov1[xf[i+1]][xf[i]] = [0, xf[i]+xf[i+1][key - 1:]]
        slov1[xf[i+1]][xf[i]][0] += 1
    return slov1

def delete_graph(grafin, bokal, kubok):
    key_out = list(bokal.keys())
    for v in key_out:
        if v not in grafin:
            continue
        if len(grafin[v]) != 1 or len(bokal[v]) != 1:
            continue
        outis = list(bokal[v].keys())[0]
        inis = list(grafin[v].keys())[0]
        strochechka = bokal[inis][v][1] + bokal[v][outis][1][kubok:]
        
        grafin[outis][inis] = [(len(grafin[v][inis][1])*grafin[v][inis][0] + len(bokal[v][outis][1])*bokal[v][outis][0])/len(strochechka), strochechka]
        bokal[inis][outis] = [(len(grafin[v][inis][1])*grafin[v][inis][0] + len(bokal[v][outis][1])*bokal[v][outis][0])/len(strochechka), strochechka]                         
        
        del grafin[v]
        del bokal[v]
        del grafin[outis][v]
        del bokal[inis][v]

    v_cov = []
    v_len = []
    for v in bokal:
        for neig in bokal[v]:
            v_cov.append(bokal[v][neig][0])
            v_len.append(len(bokal[v][neig][1]))
    return grafin, bokal, v_cov, v_len
                                  
def fastq(file):
    count = 0
    read = []
    with open(file) as inp:
        for line in inp:
            line = line.strip()
            if count % 4 == 1:
                read.append(line)
            count += 1
    return read
#print(fastq(r'C:\Users\Иванg\Downloads\s_6.first1000.fastq'))

def delete_vertices(grafin, bokal, total_cov, total_len, v_cov, v_len):
    verh = list(bokal.keys())
    for v in verh:
        n_v = list(bokal[v].keys())
        for neig in n_v:
            if bokal[v][neig][0]>=total_cov or len(bokal[v][neig][1])>=total_len:
                continue
            del v_cov[v_cov.index(bokal[v][neig][0])]
            del v_len[v_len.index(len(bokal[v][neig][1]))]
            del bokal[v][neig]
            del grafin[neig][v]

def create_de_bruijn_graph(file_n, kk):
    first = True
    for r in fastq(file_n):
        if first:
            graph = Create_graph_out(extract_Kmers(r, kk), {}, kk)
            graph1 = Create_graph_in(extract_Kmers(r, kk), {}, kk)
            first = False
        else:
            Create_graph_out(extract_Kmers(r, kk), graph, kk)
            Create_graph_in(extract_Kmers(r, kk), graph1, kk)
    graph1, graph, v_cov, v_len = delete_graph(graph1, graph, kk)
    total_cov = sum(v_cov)/len(graph)/3
    total_len = sum(v_len)/len(graph)/3
    print(len(graph))
    delete_graph(graph1, graph, kk)
    while min(v_cov) <= total_cov and min(v_len) <= total_len:
        delete_vertices(graph1, graph, total_cov, total_len, v_cov, v_len)
        graph1, graph, v_cov, v_len = delete_graph(graph1, graph, kk)
    print(len(graph))
    return (graph, graph1)
#print(create_de_bruijn_graph(r'C:\Users\Иванg\Downloads\s_6.first1000.fastq', 4))

bok, graf = create_de_bruijn_graph(r'C:\Users\Иванg\Downloads\s_6.first1000.fastq', 14)
dump_graph(bok, r'C:\Users\Иванg\Desktop\out.txt')



                   #add_kmers(out
        
    









    

    
