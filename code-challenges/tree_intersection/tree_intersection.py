from tree import BinaryTree, Node

def tree_intersection(tree1, tree2):
    if tree1.root == None or tree2.root == None: 
        return []
        
    tree1_values = tree1.in_order()

    intersection = []

    def _visit(node):
        nonlocal tree1_values
        nonlocal intersection

        if node.left:
            _visit(node.left)
    
        if node.value in tree1_values:
            intersection.append(node.value)

        if node.right:
            _visit(node.right)

    _visit(tree2.root)
    return intersection 