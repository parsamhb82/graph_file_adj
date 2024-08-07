import csv
import json
import heapq
from collections import defaultdict, deque
class Graph:
    def __init__(self, data_type, file_path = None, adj_matrix = None):
        self.adj_list = defaultdict(list)
        self.vertices = set()

        if data_type == 'adj_matrix':
            self.load_adj_matrix(adj_matrix)
        elif data_type == 'csv':
            self.load_csv(file_path)
        elif data_type == 'json':
            self.load_json(file_path)
    
    def load_csv(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            adj_matrix = [list(map(int, row)) for row in reader]
            self.load_adj_matrix(adj_matrix)

    def load_adj_matrix(self, adj_matrix):
        for i in range(len(adj_matrix)):
            for j in range(len(adj_matrix)):
                if adj_matrix[i][j] != 0 :
                    self.add_edge(i, j, adj_matrix[i][j])
    
    def load_json(self, file_path):
        with open(file_path, 'r') as file:
            edges = json.load(file)
            for edge in edges :
                self.add_edge(edge['i'], edge['j'], edge['w'])
    def add_edge(self, i, j, weight = 1):
        self.adj_list[i].append((j, weight))
        self.vertices.add(i)
        self.vertices.add(j)

    def to_csv(self, file_path):
        size = len(self.vertices)
        adj_matrix = [[0] * size for _ in range(size)]
        for u in self.adj_list:
            for v, weight in self.adj_list[u]:
                adj_matrix[u][v] = weight
        
        with open(file_path, 'w', newline= '') as file:
            writer = csv.writer(file)
            writer.writerows(adj_matrix)
    
    def to_adj_matrix(self):
        size = len(self.vertices)
        adj_matrix = [[0]*size for _ in range(size)]
        for u in self.adj_list:
            for v, weight in self.adj_list[u]:
                adj_matrix[u][v] = weight
        return adj_matrix
    
    def to_json(self, file_path):
        edges = []
        for u in self.adj_list:
            for v, weight in self.adj_list[u]:
                edges.append({'s': u, 'g': v, 'w': weight})
        
        with open(file_path, 'w') as file:
            json.dump(edges, file, indent=4)

    
    def num_vertices(self):
        return len(self.vertices)
    
    def num_edges(self):
        return sum(len(neighbors) for neighbors in self.adj_list.values())//2
    
    def all_vertices(self):
        return list(self.vertices)
    
    def BFS(self, start):
        visited = set()
        queue = deque([start])
        order = []
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                order.append(vertex)
                for neighbor, _ in self.adj_list[vertex]: #_
                    if neighbor not in visited:
                        queue.append(neighbor)
        return order
    
    def DFS(self, start):
        stack = [start]
        visited = set()
        order = []
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                order.append(vertex)
                for neighbor, _ in self.adj_list[vertex]:
                    if neighbor not in visited:
                        stack.append(neighbor)

        return order
    
    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.adj_list[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

    
def main():
    adj_matrix1 = [
        [0, 5, 3, 0, 0, 0],
        [5, 0, 0, 0, 7, 0],
        [3, 0, 0, 4, 0, 0],
        [0, 0, 4, 0, 0, 1],
        [0, 7, 0, 0, 0, 2],
        [0, 0, 0, 1, 2, 0]
        ]
    g1 = Graph(data_type='adj_matrix', file_path= None,adj_matrix = adj_matrix1 )
    print(g1.num_vertices())
    print(g1.num_edges())
    print(g1.all_vertices())
    g1.to_json("graph_json.json")
    g1.to_csv("graph_csv.csv")
    print(g1.BFS(0))
    print(g1.DFS(0))
    print(g1.dijkstra(0))
if __name__ == '__main__':
    main()


    

            