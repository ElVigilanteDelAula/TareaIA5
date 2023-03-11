from queue import PriorityQueue
import GeneradorDeInstancias as gi
import timeit



inicio = timeit.default_timer()
def dijkstra_greedy(graph, start, end):
    # Crear un conjunto vacío para nodos visitados
    visited = set()

    # Crear una cola de prioridad para nodos abiertos con valor inicial igual a la distancia
    # desde el nodo inicial hasta cada nodo en el grafo
    pq = PriorityQueue()
    for node in graph:
        dist = heuristic(node, start) 
        pq.put((dist, node))


    # Crear un diccionario para almacenar la distancia más corta conocida desde el nodo inicial
    # a cualquier nodo en el grafo
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    # Crear un diccionario para almacenar los padres de cada nodo en el camino más corto conocido desde
    # el nodo inicial a ese nodo
    parents = {}

    while not pq.empty():
        # Extraer el nodo con la distancia más baja de la cola de prioridad
        curr_dist, curr_node = pq.get()

        # Si el nodo actual es el nodo final, se ha encontrado el camino más corto
        if curr_node == end:
            # Construir el camino más corto desde el nodo final hasta el nodo inicial
            path = []
            while curr_node in parents:
                path.append(curr_node)
                curr_node = parents[curr_node]
            path.append(start)
            path.reverse()

            return path, dist[end]

        # Agregar el nodo actual al conjunto de nodos visitados
        visited.add(curr_node)

        # Para cada vecino del nodo actual
        for neighbor, weight in graph.get(curr_node, {}).items():
            # Si el vecino ya ha sido visitado, continuar con el siguiente vecino
            if neighbor in visited:
                continue

            # Calcular la distancia desde el nodo inicial hasta el vecino a través del nodo actual
            tentative_dist = dist[curr_node] + weight

            # Si la distancia calculada es menor que la distancia conocida más corta desde el nodo inicial
            # al vecino, actualizar la distancia más corta conocida y establecer el padre del vecino como el nodo actual
            if tentative_dist < dist[neighbor]:
                aux = tentative_dist
                dist[neighbor] = aux
                parents[neighbor] = curr_node

                # Actualizar el valor de la distancia en la cola de prioridad
                f = tentative_dist + heuristic(neighbor, end)
                pq.put((f, neighbor))

    # Si no se puede encontrar un camino desde el nodo inicial al nodo final, devolver None
    return None, None


def heuristic(node, start):
    x1, y1 = node
    
    x2, y2 = start
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

graph, start, end = gi.generate_instance(30)

print(dijkstra_greedy(graph, start, end))
stop = timeit.default_timer()
print('Time: ', stop - inicio)