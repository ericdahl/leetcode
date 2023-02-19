class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if p and not q or q and not p:
            return False

        if p.val != q.val:
            return False

        return Solution.isSameTree(self, p.left, q.left) and Solution.isSameTree(self, p.right, q.right)