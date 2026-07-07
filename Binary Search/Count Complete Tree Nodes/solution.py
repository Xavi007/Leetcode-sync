# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def left_height(self, node):
        h = 0
        while node:
            h += 1
            node = node.left
        return h

    def right_height(self, node):
        h = 0
        while node:
            h += 1
            node = node.right
        return h

    def countNodes(self, root):
        if not root:
            return 0

        lh = self.left_height(root)
        rh = self.right_height(root)

        if lh == rh:
            return (1 << lh) - 1   # 2^lh - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)