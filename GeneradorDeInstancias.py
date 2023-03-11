import random

def generate_instance(size):
    graph = {}
    for i in range(size):
        for j in range(size):
            node = (i, j)
            neighbors = {}
            if i > 0:
                neighbors[(i-1, j)] = random.randint(1, 10)
            if i < size-1:
                neighbors[(i+1, j)] = random.randint(1, 10)
            if j > 0:
                neighbors[(i, j-1)] = random.randint(1, 10)
            if j < size-1:
                neighbors[(i, j+1)] = random.randint(1, 10)
            graph[node] = neighbors
    return graph, (0, 0), (size-1, size-1)


