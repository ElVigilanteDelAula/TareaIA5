from queue import PriorityQueue
import GeneradorDeInstancias as gi
import timeit



inicio = timeit.default_timer()
def A_star(graph, start, end):
    # Crear un conjunto vacío para nodos visitados
   

    visited = set()

    # Crear una cola de prioridad para nodos abiertos con valor inicial
    # f = g + h, donde g es la distancia desde el nodo inicial y h es la heurística
    # estimación de la distancia restante hasta el nodo final
    pq = PriorityQueue()
    pq.put((0, start))

    # Crear un diccionario para almacenar la distancia más corta conocida desde el nodo inicial
    # a cualquier nodo en el grafo
    dist = {start: 0}

    # Crear un diccionario para almacenar los padres de cada nodo en el camino más corto conocido desde
    # el nodo inicial a ese nodo
    parents = {}

    while not pq.empty():
        # Extraer el nodo con el valor f más bajo de la cola de prioridad
        curr_node = pq.get()

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
            if neighbor not in dist or tentative_dist < dist[neighbor]:
                dist[neighbor] = tentative_dist
                parents[neighbor] = curr_node

                # Calcular el valor f para el vecino y agregarlo a la cola de prioridad
                f = tentative_dist + heuristic(neighbor, end)
                pq.put((f, neighbor))

    # Si no se puede encontrar un camino desde el nodo inicial al nodo final, devolver None
    return None, None


def heuristic(node, end):
    # Una heurística simple es la distancia euclidiana entre los nodos
    return ((node[0] - end[0]) ** 2 + (node[1] - end[1]) ** 2) ** 0.5



graph, start, end = gi.generate_instance(6)

print(A_star(graph, start, end))

stop = timeit.default_timer()
print('Time: ', stop - inicio)