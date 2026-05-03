"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:

    @staticmethod
    def build_adj_dict(node: Optional['Node']):
        d = {}
        to_visit = list([node])
        visited = set()
        while to_visit and to_visit[0]:
            
            n = to_visit.pop()
            visited.add(n)
            neighbor_vals = []
            for neighbor in n.neighbors:
                neighbor_vals.append(neighbor.val)
                if not neighbor in visited:
                    to_visit.append(neighbor)
            d[n.val] = neighbor_vals

        return d

    @staticmethod
    def init_clones(d_adj_values: dict[int, [int]]) -> dict:
        d_nodes = {}
        for (node_val, node_neighbor_vals) in d_adj_values.items():
            n = Node(node_val, [])
            d_nodes[node_val] = n
        return d_nodes

    @staticmethod
    def populate_neighbors(d_adj_values: dict[int, [int]], clones: dict) -> None:
        for (node_val, node) in clones.items():
            for neighbor_value in d_adj_values[node_val]:
                node.neighbors.append(clones[neighbor_value])

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        d_adj_values = Solution.build_adj_dict(node)
        clones = Solution.init_clones(d_adj_values)
        Solution.populate_neighbors(d_adj_values, clones)

        return clones[node.val]

        
