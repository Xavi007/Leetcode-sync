# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.IsSame(root.left, root.right)

    def IsSame(self, p, q):
        # If both nodes are None
        if not p and not q:
            return True
        
        # If one of them is None
        if not p or not q:
            return False
        
        # If values are different
        if p.val != q.val:
            return False
        
        # Recursively check left and right
        return self.IsSame(p.left, q.right) and self.IsSame(p.right, q.left)
