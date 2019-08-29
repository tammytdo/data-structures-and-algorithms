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


class BinarySearchTree:
    def __init__(self, node=None):
        self.root = node

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else: 
            self._insert_node(value, self.root)

    def _insert_node(self, value, current_node):
        if value < current_node.value:
            if current_node.left == None:
                current_node.left = Node(value)
            else:
                self._insert_node(value, current_node.left)
        elif value > current_node.value:
            if current_node.right == None:
                current_node.right = Node(value)
            else:
                self._insert_node(value, current_node.right)
        else:
            return None
     
    def contains(self, value):
    
        def contains_finder(node, value):
            if node.value == value:
                return True
            elif value < node.value and node.left:
                return contains_finder(node.left, value)
            elif value > node.value and node.right:
                return contains_finder(node.right, value)
            
        return contains_finder(self.root, value) or False
    
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