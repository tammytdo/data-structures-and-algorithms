from tree import BinaryTree, Node

def tree_intersection(tree1, tree2):
    if tree1.root == None or tree2.root == None: 
        return []
        
    tree1_values = tree1.in_order()
    print('tree1_values:', tree1_values)

    intersection = []

    def _visit(node):
        nonlocal tree1_values
        nonlocal intersection

        if node.left:
            _visit(node.left)
    
        if node.value in tree1_values:
            intersection.append(node)

        if node.right:
            _visit(node.right)

    _visit(tree2.root)
    print('intersection:', intersection)

    return intersection 


# from tree import BinaryTree, Node

# def tree_intersection(tree1, tree2):
#     if tree1.root == None or tree2.root == None: 
#         return []
        
#     tree1_values = tree1.in_order()
#     tree2_values = tree2.in_order()

#     intersection = []

#     for i in tree2_values:
#         if i in tree1_values:
#             intersection.append(i)

#     return intersection 