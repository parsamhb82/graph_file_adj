# graph_file_adj
graph that reads csv or json file or an adj_matrix
import csv
import json
import heapq
from collections import defaultdict, deque
class Graph:
    fateme:
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

    def load_adj_matrix(self, adj_matrix):
    def load_json(self, file_path):
    def add_edge(self, i, j, weight):
    aria
    def to_csv(self, file_path):
    
    def to_adj_matrix(self):
    
    def to_json(self, file_path):

    
    def num_vertices(self):
        return len(self.vertices)
    
    def num_edges(self):
        return sum(len(neighbors) for neighbors in self.adj_list.values())//2
    
    def all_vertices(self):
        return list(self.vertices)
    parsa:
    def BFS(self, start):
    
    def DFS(self, start):
    
    def dijkstra(self, start):


    
def main():sara
if __name__ == '__main__':
    main()


    

            
    
