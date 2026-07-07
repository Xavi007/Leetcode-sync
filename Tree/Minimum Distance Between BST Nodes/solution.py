
class Solution:
    def __init__(self):
        self.prev = None

    def minDiffInBST(self, root):
        if root is None:
            return float('inf')

        ans = float('inf')

        if root.left:
            left_min = self.minDiffInBST(root.left)
            ans = min(ans, left_min)

        if self.prev:
            ans = min(ans, root.val - self.prev.val)

        self.prev = root

        if root.right:
            right_min = self.minDiffInBST(root.right)
            ans = min(ans, right_min)

        return ans