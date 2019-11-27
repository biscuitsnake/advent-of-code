input = open("8.txt").read()

tree = input.split(" ")
tree = list(map(int, tree))

test = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

#node: [children, metadata entries []]

total = 0

# [0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2]
def many_nodes(node, child_count)
    noded = False
    while not noded:
        child
        


def single_node(node):
    data = node[:2]
    metadata = node[-node[1]:]
    children = node[2:-node[1]]

    total += sum(metadata)

    if children[1] + 2 == len(children):
        single_node(children)
    elif children[1] + 2 > len(children):
        many_nodes(children, data[0])
    else:
        pass

    
   
    
