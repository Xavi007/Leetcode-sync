# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        idx = {}

        for i, val in enumerate(inorder):
            idx[val] = i

        def construct(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None

            root = TreeNode(preorder[pre_start])

            in_root = idx[root.val]
            left_count = in_root - in_start

            root.left = construct(pre_start + 1, pre_start + left_count,
                in_start,in_root - 1)

            root.right = construct(pre_start + left_count + 1, pre_end,
                in_root + 1, in_end)

            return root

        return construct(0, len(preorder) - 1, 0, len(inorder) - 1)