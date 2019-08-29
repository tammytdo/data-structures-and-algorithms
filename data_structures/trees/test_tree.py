from tree import Node, BinaryTree, BinarySearchTree
import pytest

@pytest.fixture()
def tree():
    ten = Node(10)
    five = Node(5)
    two = Node(2)
    seven = Node(7)
    six = Node(6)
    nine = Node(9)
    twenty = Node(20)
    fifteen = Node(15)
    thirty = Node(30)

    ten.left = five
    ten.right = twenty
    five.left = two
    five.right = seven
    seven.left = six
    seven.right = nine
    twenty.left = fifteen
    twenty.right = thirty
    
    return BinarySearchTree(ten)

def test_classes_exist():
    assert Node
    assert BinaryTree
    assert BinarySearchTree

def test_BinaryTree_empty():
    assert BinaryTree().root == None

def test_BinaryTree_with_root():
    node = Node(10)
    tree = BinaryTree(node)

    assert tree.root.value == 10

def test_BinaryTree_root_left():
    node = Node(10)
    node.left = Node(5)
    node.right = Node(20)
    tree = BinaryTree(node)
    
    assert tree.root.left.value == 5

def test_BinaryTree_root_right():
    node = Node(10)
    node.left = Node(5)
    node.right = Node(20)
    tree = BinaryTree(node)
    
    assert tree.root.right.value == 20

def test_BinaryTree_contains(tree):
    assert tree.contains(10) == True
    assert tree.contains(20) == True
    assert tree.contains(30) == True
    assert tree.contains(11) == False

def test_pre_order(tree):
    assert tree.pre_order() == [10, 5, 2, 7, 6, 9, 20, 15, 30]

def test_in_order(tree):
    assert tree.in_order() == [2, 5, 6, 7, 9, 10, 15, 20, 30]

def test_post_order(tree):
    assert tree.post_order() == [2, 6, 9, 7, 5, 15, 30, 20, 10]