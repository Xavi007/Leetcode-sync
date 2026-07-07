# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.queue = []

        def preorder(node):
            if not node:
                return
            self.queue.append(node)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        if self.queue:
            self.queue.pop(0)
            while self.queue:
                root.right = self.queue.pop(0)
                root.left = None
                root = root.right
