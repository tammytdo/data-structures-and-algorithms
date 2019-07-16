from linked_list import LinkedList, Node
import pytest

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
    assert ll.includes('rojo') == False

def test__str__():
    ll = LinkedList()
    ll.insert('violet')
    ll.insert('indigo')
    ll.insert('blue')
    assert ll.__str__() == 'blue indigo violet '

def test_append():
    ll = LinkedList()
    ll.insert('violet')
    ll.insert('indigo')
    ll.insert('blue')
    ll.append('green')
    assert ll.head.next.next.next.value =='green'

def test_includes_before():
    ll = LinkedList()
    ll.insert('violet')
    ll.insert('indigo')
    ll.insert('blue')
    ll.insert_before('violet', 'green')
    assert ll.head.next.next.value == 'green'

def test_insert_after():
    ll = LinkedList()
    ll.insert('violet')
    ll.insert('indigo')
    ll.insert('blue')
    ll.insert_after('indigo', 'green')
    assert ll.head.next.next.value == 'green'

