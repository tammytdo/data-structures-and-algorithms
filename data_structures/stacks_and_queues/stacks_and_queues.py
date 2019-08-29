class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        self.head = Node(value, self.head)


class Stack:
    def __init__(self):
        self.top = None
        self._lst = LinkedList()

    def push(self, value):
        self._lst.insert(value)
        self.top = self._lst.head

    def pop(self):
        if self.top:
            node_to_pop = self._lst.head
            self.top = self._lst.head.next
            self._lst.head = self._lst.head.next

            return node_to_pop.value

        else:
            return None

    def peek(self):
        if self.top:
            return self.top and self.top.value
        else:
            raise ValueError

class Queue:
    
    def __init__(self):
        self.front = None
        self.back = None
        self._lst = LinkedList()

    def enqueue(self, value):
        node = Node(value)
         
        if self.front:
            self.back.next = node
            self.back = node

        else:
            self.front = node
            self.back = node

    def dequeue(self):
        if self.front:
            reference = self.front.value
            self.front = self.front.next
            return reference
        else:
            return None

    def peek(self):
        if self.front:
            return self.front.value
        else:
            return None