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
    print(cur_v)
    for neig in listik[cur_v]:
        if not visited[neig] and neig not in stack:
            stack.append(neig)
    if x[cur_v]>maxik:
        maxik = x[cur_v]
        maxv = cur_v
print(maxik, maxv)

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
    print(cur_v)
    for neig in listik[cur_v]:
        if not visited[neig] and neig not in queue:
            queue.append(neig)
    if x[cur_v]>maxik:
        maxik = x[cur_v]
        maxv = cur_v
print(maxik, maxv)

    
