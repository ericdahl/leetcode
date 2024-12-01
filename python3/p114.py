class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Flattens the tree in-place without using nonlocal.
        """
        if not root:
            return

        def flatten(node: Optional[TreeNode], prev: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return prev

            prev = flatten(node.right, prev)
            prev = flatten(node.left, prev)

            node.right = prev
            node.left = None
            return node

        flatten(root, None)
