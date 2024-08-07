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
    