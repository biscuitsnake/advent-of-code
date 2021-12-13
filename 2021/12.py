from collections import defaultdict

puzzle = [i.strip().split("-") for i in open("12.txt").readlines()]
graph = defaultdict(list)

for path in puzzle:
    graph[path[0]].append(path[1])
    graph[path[1]].append(path[0])

def search(node, visited):
    if node == "end":
        paths.append(visited)
    visited.append(node)
    for n in graph[node]:
        if n.isupper() or n not in visited:
            search(n, visited.copy())

paths = []
search("start", [])
print(len(paths))
