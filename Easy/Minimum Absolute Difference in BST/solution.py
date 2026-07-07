# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.prev = None


    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return float('inf')

        ans = float('inf')

        if root.left:
            left_min = self.getMinimumDifference(root.left)
            ans = min(ans, left_min)

        if self.prev:
            ans = min(ans, root.val - self.prev.val)

        self.prev = root

        if root.right:
            right_min = self.getMinimumDifference(root.right)
            ans = min(ans, right_min)

        return ans