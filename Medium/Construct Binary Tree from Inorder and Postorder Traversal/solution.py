# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        idx = {}

        for i, val in enumerate(inorder):
            idx[val] = i

        def construct(in_start, in_end, post_start, post_end):
            if in_start > in_end or post_start > post_end:
                return None

            root = TreeNode(postorder[post_end])

            in_root = idx[root.val]
            right_count = in_end - in_root

            root.right = construct(in_root + 1, in_end,
                post_end - right_count, post_end - 1 )

            root.left = construct( in_start, in_root - 1,
                post_start, post_end - right_count - 1 )

            return root

        return construct(0, len(inorder) - 1, 0, len(postorder) - 1)