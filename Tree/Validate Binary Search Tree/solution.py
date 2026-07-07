# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: Optional[TreeNode], min_val: Optional[TreeNode],max_val: Optional[TreeNode]):
        if(root == None):
            return True

        if((min_val != None) and (root.val <= min_val.val)):
            return False

        if((max_val != None) and (root.val  >= max_val.val)):
            return False

        return self.helper(root.left, min_val, root) and self.helper(root.right, root, max_val)


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, None, None)
        