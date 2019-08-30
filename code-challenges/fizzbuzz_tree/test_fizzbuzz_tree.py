from fizzbuzz_tree import fizz_buzz_tree
from tree import BinaryTree, Node
import pytest

@pytest.fixture()
def tree():
    ten = Node(10)

    ten.left = Node(3)
    ten.right = Node(5)
    ten.left.left = Node(6)
    ten.left.right = Node(9)
    ten.right.right = Node(10)
    ten.right.left = Node(15)

    tree = BinaryTree()
    tree.root = ten

    return tree

def test_exists():
    assert fizz_buzz_tree
    assert BinaryTree
    assert Node

def test_root(tree):
    assert tree.root.value == 10

def test_tree_empty():
    tree = BinaryTree()
    fb_tree = fizz_buzz_tree(tree)
    assert fb_tree.root == None

def test_root_children(tree):
    assert tree.root.left.value == 3
    assert tree.root.right.value == 5

def test_traverse_tree(tree):
    assert tree.root.left.value == 3
    assert tree.root.right.value == 5
    assert tree.root.left.left.value == 6
    assert tree.root.left.right.value == 9
    assert tree.root.right.right.value == 10
    assert tree.root.right.left.value == 15

def test_fizzbuzzed_tree(tree):
    fb_tree = fizz_buzz_tree(tree)
    assert fb_tree.root.left.value == 'fizz'
    assert fb_tree.root.right.value == 'buzz'
    assert fb_tree.root.left.left.value == 'fizz'
    assert fb_tree.root.left.right.value == 'fizz'
    assert fb_tree.root.right.right.value == 'buzz'
    assert fb_tree.root.right.left.value == 'fizzbuzz'

