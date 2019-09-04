from tree_intersection import tree_intersection
from tree import BinaryTree, Node
import pytest

@pytest.fixture()
def tree1():
    fifteen = Node(15)
    ten = Node(10)
    seven = Node(7)
    sixteen = Node(16)
    twelve = Node(12)
    seventeen = Node(17)
    twenty_five = Node(25)
    twenty = Node(20)
    thirty_five = Node(35)
    thirty = Node(30)
    fifty = Node(50)

    fifteen.left = ten
    ten.left = seven
    ten.right = sixteen
    sixteen.left = twelve
    sixteen.right = seventeen
    fifteen.right = twenty_five
    twenty_five.left = twenty
    twenty_five.right = thirty_five
    thirty_five.left = thirty
    thirty_five.right = fifty

    return BinaryTree(fifteen)


@pytest.fixture()
def tree2():
    four = Node(4)
    ten = Node(10)
    one = Node(1)
    sixteen = Node(16)
    twelve = Node(12)
    seventeen = Node(17)
    sixty = Node(60)
    twenty = Node(20)
    thirty_five = Node(35)
    fifty = Node(50)

    four.left = ten
    ten.left = one
    ten.right = sixteen
    sixteen.left = twelve
    sixteen.right = seventeen
    four.right = sixty
    sixty.left = twenty
    sixty.right = thirty_five
    thirty_five.right = fifty

    return BinaryTree(four)

@pytest.fixture()
def tree3():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    seven = Node(7)

    one.left = two
    one.right = three
    three.left = four
    three.right = seven    

    return BinaryTree(one)

def test_exists():
    assert tree_intersection

def test_empty_tree():
    empty_tree1 = BinaryTree()
    empty_tree2 = BinaryTree()
    test = tree_intersection(empty_tree1, empty_tree2)
    assert test == []

def test_intersection1(tree1, tree2):
    assert tree_intersection(tree1, tree2) == [10, 12, 16, 17, 20, 35, 50]

def test_intersection2(tree1, tree3):
    assert tree_intersection(tree1, tree3) == [7]