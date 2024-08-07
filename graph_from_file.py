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
    