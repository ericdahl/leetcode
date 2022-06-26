# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @staticmethod
    def traverse(root: TreeNode, visited):
        if not root:
            return

        Solution.traverse(root.left, visited)
        visited.append(root.val)
        Solution.traverse(root.right, visited)


    @staticmethod
    def build_tree(tree: TreeNode, values: int) -> TreeNode:

        if not values:
            return tree

        left_values = values[:len(values) // 2]
        right_values = values[len(values) // 2:]
        middle_value = right_values.pop(0)

        left_tree = Solution.build_tree(tree, left_values)
        right_tree = Solution.build_tree(tree, right_values)

        return TreeNode(middle_value, left_tree, right_tree)


    def balanceBST(self, root: TreeNode) -> TreeNode:

        values = []
        Solution.traverse(root, values)

        return Solution.build_tree(None, values)
