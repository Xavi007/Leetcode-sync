class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.push_all(root)

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        node = self.stack.pop()
        self.push_all(node.right)
        return node.val

    def push_all(self, node):
        while node:
            self.stack.append(node)
            node = node.left