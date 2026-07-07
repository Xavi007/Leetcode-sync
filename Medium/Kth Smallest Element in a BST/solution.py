# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    preOrder = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if(root == None):
            return -1

        if (root.left != None):
            leftAns = self.kthSmallest(root.left, k)
            if (leftAns != -1):
                return leftAns

        if(self.preOrder+1 == k):
            return root.val
        self.preOrder = self.preOrder + 1
        
        if (root.right != None):
            rightAns = self.kthSmallest(root.right, k)
            if (rightAns != -1):
                return rightAns

        return -1