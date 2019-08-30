# Trees
A binary tree is a type of tree that contains up to 2 children. Each child node can only have two children.

A binary search tree is a type of tree that contains up to 2 children with structure added to it. All child values that are smaller than the root are placed to the left, and all values that are larger than the root are placed to the right.

## Challenge
Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

Create a BinaryTree class
-Define a method for each of the depth first traversals called preOrder, inOrder, and postOrder which returns an array of the values, ordered appropriately.

Create a BinarySearchTree class
-Define a method named add that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
-Define a method named contains that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.

## API
-add(): adds new node to the binary search tree in its correct place
-contains(): returns boolean of whether node is in tree
-pre_order(): Returns a list of traversed nodes in the order of self, left, right.
-in_order(): Returns a list of traversed nodes in the order of left, self, right.
-post_order(): Returns a list of traversed nodes in the order of left, right, self.