class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, node=None):
        self.root = node

    def pre_order(self):
        visited = []

        def _visit(node):
            visited.append(node.value)

            if node.left:
                _visit(node.left)

            if node.right:
                _visit(node.right)

        _visit(self.root)
        return visited

    def in_order(self):
        visited = []

        def _visit(node):
            if node.left:
                _visit(node.left)

            visited.append(node.value)

            if node.right:
                _visit(node.right)
            
        _visit(self.root)
        return visited

    def post_order(self):
        visited = []
        
        def _visit(node):
            if node.left:
                _visit(node.left)
            if node.right:
                _visit(node.right)
            
            visited.append(node.value)
        
        _visit(self.root)
        return visited