# Stacks and Queues
A stack is a data structure with a collection of node objects that supports fast last-in, first-out (LIFO) semantics for inserts and deletes. Each Node references the next node in the stack, but does not reference it’s previous.

A queue is a data structure with a collection of node objects that supports the concept of first-in, first-out (FIFO). Each Node references the next node in the stack, but does not reference it’s previous.

## Challenge
-Create a Stack class
-Create a Queue class

## Approach & Efficiency
Approach
Big O space: O(1)
Big O time: O(1)

## API
Stack:
-push() which takes any value as an argument and adds a new node with that value to the top of the stack.
-pop() that does not take any argument, removes the node from the top of the stack, and returns the node’s value.
-peek() that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.

Queue:
-enqueue() which takes any value as an argument and adds a new node with that value to the back of the queue.
-dequeue() that does not take any argument, removes the node from the front of the queue, and returns the node’s value.
-peek() that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.