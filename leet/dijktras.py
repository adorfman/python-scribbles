import heapq

path = {}
root = path

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    path[start] = {}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        # {'A': {'B': {}, 'C': {}}, 'B': {'D': {}}, 'C': {}, 'D': {}}
        root = root[current_node]

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                #path[current_node].setdefault( neighbor, {} )
                root[neighbor] = {}
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example usage:
graph = {
    'A': {'B': 1, 'C': 1},
    'B': {'A': 1, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 2},
    'D': {'B': 1, 'C': 2}
}
print(dijkstra(graph, 'A'))
print(path)
