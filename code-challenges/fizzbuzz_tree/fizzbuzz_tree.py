def fizz_buzz_tree(tree):

    def _visit(node):
        if node.value % 3 == 0 and node.value % 5 == 0:
            node.value = 'fizzbuzz'

        elif node.value % 3 == 0:
            node.value = 'fizz'
        
        elif node.value % 5 == 0:
            node.value = 'buzz'
        else:
            node.value = node.value

        if node.left:
            _visit(node.left)
        if node.right:
            _visit(node.right)

    if tree.root:
        _visit(tree.root)
            
    return tree
