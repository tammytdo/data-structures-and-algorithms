from linked_list import LinkedList, Node

# Write tests to prove the following functionality:

# Can successfully instantiate an empty linked list
def test_exists(): 
    assert LinkedList

def test_insert():
    ll = LinkedList()
    ll.insert('violet')
    assert ll.head.value == 'violet'

def test_insert_many():
    ll = LinkedList()
    ll.insert('violet')
    ll.insert('indigo')
    ll.insert('blue')
    assert ll.head.value == 'blue'
    assert ll.head.next.value == 'indigo'

def test_includes():
    ll = LinkedList()
    ll.insert('violet')
    ll.insert('indigo')
    ll.insert('blue')
    assert ll.includes('indigo') == True
    assert ll.includes(4) == False

def test__str__():
    ll = LinkedList()
    ll.insert('violet')
    ll.insert('indigo')
    ll.insert('blue')
    assert ll.__str__() == 'blue indigo violet '


# Can properly return a collection of all the values that exist in the linked list