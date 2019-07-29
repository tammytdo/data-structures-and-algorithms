class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        values = []

        def visit(node):
            values.append(node.value)

            if node.left_child:
                visit(node.left_child)
            if node.right_child:
                visit(node.right_child)

        visit(self.root)
        return values 

    def in_order(self):
        values = []

        def visit(node):
            if node.left_child:
                visit(node.left_child)

            values.append(node.value)

            if node.right_child:
                visit(node.right_child)
            
        visit(self.root)
        return values

    def post_order(self):
        values = []
        
        def visit(node):
            if node.left_child:
                visit(node.left_child)
            if node.right_child:
                visit(node.right_child)
            
            values.append(node.value)
        
        visit(self.root)
        return values

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        pass
        
    def contains(self, value):
        pass


# Define a method named add that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
# Define a method named contains that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once. 