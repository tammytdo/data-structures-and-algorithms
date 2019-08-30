import pytest
from stacks_and_queues import LinkedList, Node, Stack, Queue


def test_stack_exists():
    assert Stack()

def test_queue_exists():
    assert Queue()

def test_linkedlist_exists():
    assert LinkedList()

def test_node_exists():
    assert Node(1)

def test_stack_push_one():
    s = Stack()
    s.push('1')

    assert s.top.value == '1'

def test_stack_push_mult():
    s = Stack()
    s.push('1')
    s.push('2')
    s.push('3')
    s.push('4')

    assert s.top.value == '4'

def test_stack_push_empty():
    s = Stack()

    assert s.top == None

def test_stack_pop_one():
    s = Stack()
    s.push('1')

    assert s.pop() == '1'

def test_stack_pop_many():
    s = Stack()
    s.push('1')
    s.push('2')
    s.push('3')
    s.push('4')

    assert s.pop() == '4'
    assert s.pop() == '3'
    assert s.pop() == '2'
    assert s.pop() == '1'

def test_stack_pop_until_empty():
    s = Stack()
    s.push('1')
    s.push('2')

    assert s.pop() == '2'
    assert s.pop() == '1'
    assert s.pop() == None


def test_stack_peek():
    s = Stack()
    s.push('1')
    s.push('2')

    assert s.peek() == '2'

def test_empty_queue():
    q = Queue()
    assert q.front == None

def test_enqueue():
    q = Queue()
    q.enqueue('1')
    q.enqueue('2')
    q.enqueue('3')

    assert q.peek() == '1'

def test_dequeue():
    q = Queue()
    q.enqueue('1')
    q.enqueue('2')
    q.enqueue('3')
    
    assert q.dequeue() == '1'
    assert q.dequeue() == '2'
    assert q.dequeue() == '3'
    assert q.peek() == None