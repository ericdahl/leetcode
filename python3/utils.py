class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def print_tree(node: TreeNode, level = 0):
        # print(f"print_tree({node}, {level})")
        if node:
            Solution.print_tree(node.left, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.val))
            Solution.print_tree(node.right, level + 1)