# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def traverse(root):
            if not root:
                return [None]

            return [root.val] + traverse(root.left) + traverse(root.right)

        return str(traverse(root))


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        l = []
        for token in data[1:-1].split(','):
            if token == '':
                continue
            if 'None' in token:
                l.append(None)
            else:
                l.append(int(token))

        def traverse(l):
            if not l:
                return None

            curr = l.pop(0)

            if curr is not None:
                node = TreeNode(curr)
                node.left = traverse(l)
                node.right = traverse(l)
                return node
            else:
                return None

        return traverse(l)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))