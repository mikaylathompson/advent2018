import random
import string

class Node():
    def __init__(self, n_children, n_meta, label=""):
        self.n_children = n_children
        self.n_meta = n_meta
        self.children = [] 
        self.metas = []
        self.label = label

    def add_child(self, child):
        if len(self.children) >= self.n_children:
            print(f"({self.label}) Possibly a problem. More children added than should exist.")
        self.children.append(child)

    def __repr__(self):
        return f"(([{self.label}] {str([c.label for c in self.children])} {str(self.metas)}))"
    
    def sum_metas(self):
        return sum(self.metas) + sum([n.sum_metas() for n in self.children])

    def value(self):
        if self.n_children == 0:
            return sum(self.metas)
        running_sum = 0
        for m in self.metas:
            if m == 0:
                running_sum += 0
                continue
            try:
                running_sum += self.children[m-1].value()
            except IndexError:
                running_sum += 0
        return running_sum


# This label stuff is totally unnecessary! It's just to help myself with debugging.
def get_label():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
            
def process_recursively(node):
    # print("Looking at the node text: ", node)
    n = Node(int(node[0]), int(node[1]), label=get_label())
    # print(f"Initiated a node ({n.label}) with {node[0]} children and {node[1]} meta")
    active = n.label
    remaining_children = n.n_children
    pointer = 2 # first relevant position in node
    while remaining_children > 0:
        child, pointer_jump = process_recursively(node[pointer:])
        n.add_child(child)
        pointer += pointer_jump
        remaining_children -= 1

    # print(f"({active}) Looking for {n.n_meta} meta: {node[pointer:pointer + n.n_meta]}")
    n.metas = list(map(int, node[pointer:pointer + n.n_meta]))
    return n, pointer + n.n_meta


def fn1(inpt):
    node, pointer = process_recursively(inpt)
    print(node)
    return node.sum_metas()

def fn2(inpt):
    node, pointer = process_recursively(inpt)
    print(node)
    return node.value()

if __name__ == "__main__":
    # sample = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split()
    # print(fn1(sample))
    # print(fn2(sample))
    with open('day8_2018.txt', 'r') as f:
        print(fn1(f.read().strip().split()))
        f.seek(0)
        print(fn2(f.read().strip().split()))
