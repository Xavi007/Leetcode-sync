# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, path):
        if not node:
            return 0
        path = 10 * path + node.val
        if not node.left and not node.right:
            return path
        return self.dfs(node.left, path) + self.dfs(node.right, path)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)