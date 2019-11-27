import networkx

lines = open("7.txt").readlines()

nodes = []
for l in lines:
    nodes.append((l[5], l[36]))

graph = networkx.DiGraph(nodes)

l = networkx.lexicographical_topological_sort(graph)

order = ''

for i in list(l):
    order += i

print(order)
