from tree_intersection import tree_intersection
from tree import BinaryTree
import pytest

@pytest.fixture():
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


@pytest.fixture():
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
    four = Node(4)
    fifty = Node(50)

    four.left = ten
    ten.left = fifteen
    ten.right = sixteen
    sixteen.left = twelve
    sixteen.right = seventeen
    four.right = sixty
    sixty.left = twenty
    sixty.right = thirty_five
    thirty_five.left = four
    thirty_five.right = fifty

    return BinaryTree(four)


# def test_tree_intersection(tree1, tree2):
#     assert 