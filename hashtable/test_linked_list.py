from linked_list import LinkedList, Node

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