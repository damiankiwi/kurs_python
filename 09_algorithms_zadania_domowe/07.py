import sys

def dijkstra(graph, start):
    distances = {node: sys.maxsize for node in graph}
    distances[start] = 0
    visited = set()

    while visited != set(graph):
        min_distance = sys.maxsize
        min_node = None
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node

        for neighbor, weight in graph[min_node].items():
            distance = distances[min_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.add(min_node)

    return distances

graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 1, 'D': 2},
    'C': {'A': 3, 'B': 1, 'D': 4, 'E': 8},
    'D': {'B': 2, 'C': 4, 'E': 2, 'F': 2},
    'E': {'C': 8, 'D': 2, 'F': 6},
    'F': {'D': 2, 'E': 6}
}

start_node = 'A'

distances = dijkstra(graph, start_node)

print("Najkrótsze ścieżki od wierzchołka", start_node)
for node, distance in distances.items():
    print("Do wierzchołka", node, "odległość wynosi:", distance)