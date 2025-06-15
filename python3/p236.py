# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        def traverse(root: 'TreeNode', target:int) -> List[TreeNode]:
            if not root:
                return []

            if root.val == target:
                return [root]

            left = traverse(root.left, target)
            if left:
                return [root] + left

            right = traverse(root.right, target)
            if right:
                return [root] + right

            return []


        p_path = traverse(root, p.val)
        q_path = traverse(root, q.val)

        lca = None
        for i in range(min(len(p_path), len(q_path))):
            if p_path[i] == q_path[i]:
                lca = p_path[i]
            else:
                break

        return lca


