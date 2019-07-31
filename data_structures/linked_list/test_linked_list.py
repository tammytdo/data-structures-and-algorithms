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

def test_kth_from_end_exists():
    assert LinkedList.kth_from_end

def test_merge_lists_exists():
    assert LinkedList.merge_lists

def test_merge_lists_even_lists():
    list_a = LinkedList()
    list_b = LinkedList()

    list_a.insert('3')
    list_a.insert('2')
    list_a.insert('1')
    list_b.insert('c')
    list_b.insert('b')
    list_b.insert('a')
    list_a.merge_lists(list_a, list_b)

    assert list_a.head.value == '1'

def test_merge_lists_uneven_lists():
    list_a = LinkedList()
    list_b = LinkedList()

    list_a.insert('4')
    list_a.insert('3')
    list_a.insert('2')
    list_a.insert('1')
    list_b.insert('b')
    list_b.insert('a')
    list_a.merge_lists(list_a, list_b)

    assert list_a.head.value == '1'
    assert list_a.head.next.value == 'b'

def test_kth_from_end():
    ll = LinkedList()
    ll.insert('violet')
    ll.insert('indigo')
    ll.insert('green')
    ll.insert('blue')
    ll.kth_from_end(1)
    assert ll.head.next.value == 'green'