class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        class Node:
            def __init__(self, val):
                self.val = val
                self.left = None
                self.right = None
                self.parent = None

        class SegmentTree:
            def __init__(self, arr):
                self.root = self.build(arr, 0, len(arr) - 1)

            def build(self, arr, l, r):
                if l == r: return Node(arr[l])
                m = l + (r - l) // 2
                left = self.build(arr, l, m)
                right = self.build(arr, m + 1, r)
                node = Node(max(left.val, right.val))
                node.left = left
                node.right = right
                left.parent = right.parent = node
                return node

            def find(self, x, node=None):
                if not node or node.val < x: return None
                if not node.left and not node.right: return node
                left = self.find(x, node.left)
                if left: return left
                return self.find(x, node.right)
            
            def update(self, node, x):
                if not node: return
                lmax = float('-inf') if not node.left else node.left.val
                rmax = float('-inf') if not node.right else node.right.val
                node.val = max(x, lmax, rmax)
                self.update(node.parent, node.val)

        ans = 0
        tree = SegmentTree(baskets)
        for x in fruits:
            node = tree.find(x, tree.root)
            if not node: ans += 1
            else: tree.update(node, float('-inf'))
        return ans