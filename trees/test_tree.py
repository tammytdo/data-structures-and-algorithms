from tree import Node, BinaryTree, BinarySearchTree
import pytest

@pytest.fixture()
def create_tree():
    one = Node(1)
    five = Node(5)
    ten = Node(10)
    fifteen = Node(15)
    twenty = Node(20)
    twentyfive = Node(25)
    thirty = Node(30)
    thirtyfive = Node(35)
    fourty = Node(40)

def test_BinaryTree_single_root():
    # assert BinaryTree().root == one

def test_BinaryTree_exists():
    assert BinaryTree

def test_BinarySearchTree_exists():
    assert BinarySearchTree

# Can successfully instantiate a tree with a single root node


    assert BinaryTree

def test_BinarySearchTree_single_root():
    assert BinarySearchTree


# Can successfully add a left child and right child to a single root node
# Can successfully return a collection from a preorder traversal
# Can successfully return a collection from an inorder traversal
# Can successfully return a collection from a postorder traversal
