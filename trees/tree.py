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

        def _visit(node):
            values.append(node.value)

            if node.left_child:
                _visit(node.left_child)
            if node.right_child:
                _visit(node.right_child)

        _visit(self.root)
        return values 

    def in_order(self):
        values = []

        def _visit(node):
            if _visit.left_child:
                _visit(node.left_child)

            values.append(node.value)

            if node.right_child:
                _visit(node.right_child)
            
        _visit(self.root)
        return values

    def post_order(self):
        values = []
        
        def _visit(node):
            if node.left_child:
                _visit(node.left_child)
            if node.right_child:
                _visit(node.right_child)
            
            values.append(node.value)
        
        _visit(self.root)
        return values

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # adds a new node with that value in the correct location
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else: 
            self._insert_node(value, self.root)

    def _insert_node(self, value, current_node):
        if value < current_node.value:
            if current_node.left_child == None:
                current_node.left_child = Node(value)
            else:
                self._insert_node(value, current_node.right_child)
        elif value > current_node.value:
            if current_node.right_child == None:
                current_node.right_child = Node(value)
            else:
                self._insert_node(value, current_node.right_child)
        else:
            return "Node value already in tree"
     
    def contains(self, value):
        if self.root:
            return self._find_node(value, self.root)
        else:
            return False
    
    def _find_node(self, value, current_node):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left_child != None:
            self._find_node(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child != None:
            self._find_node(value, current_node.right_child)
        return False

def fizz_buzz_tree(tree):

    def _visit(node):
        if node.value % 3 == 0 and node.value % 5 == 0:
            node.value = 'FizzBuzz'

        elif node.value % 3 == 0:
            node.value = 'fizz'
        
        elif node.value % 5 == 0:
            node.value = 'buzz'
        else:
            node.value = node.value

    if node.left_child:
        _visit(node.left_child)
    if node.right_child:
        _visit(node.right_child)
    
    return _visit(tree.root)