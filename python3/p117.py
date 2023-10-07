"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:

    @staticmethod
    def traverse(root: 'Optional[Node]', level: int, visited:'list[list[Node]]') -> None:
        if not root:
            return

        if level >= len(visited):
            visited.append([])

        visited[level].append(root)
        Solution.traverse(root.left, level + 1, visited)
        Solution.traverse(root.right, level + 1, visited)


    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        visited = []
        Solution.traverse(root, 0, visited)

        for visited_level in visited:
            for i in range(0, len(visited_level) - 1):
                visited_level[i].next=visited_level[i + 1]

        return root