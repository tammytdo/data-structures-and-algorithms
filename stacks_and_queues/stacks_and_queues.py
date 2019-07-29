class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        new_node = Node(value)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

class Stack:
    def __init__(self):
        self.top = None
        self._lst = LinkedList()

    def push(self, value):
        self._lst.insert(value)

    def pop(self):
        node_to_pop = self._lst.head
        self.top = self._lst.head.next
        self._lst.head = self._lst.head.next

        return node_to_pop.value

    def peek(self):
        if self.top:
            return self.top.value 
        else:
            return None

class Queue:
    
    def __init__(self):
        self.front = None
        self.back = None
        self._lst = LinkedList()

    def enqueue(self, value):
        node = Node(value)
         
        if self.front:
            while self.front.next:
                placeholder = self.front 
                placeholder.next = self.front.next
                placeholder = placeholder.next
            self.back = self.front
            self.back.next = node.value
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