class LinkedList():

    def __init__(self):
        self.head = None
    
    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, key_value):
        current = self.head
        while current:
            if current.value == key_value:
                return True
            if current.value != key_value:
    
                new_current = current.next
                current = new_current
        return False

    def __str__(self):
        if self.head.value == None:
            return 'Error string'
        current = self.head
        list_result = ''
        while True:
            try: 
                if current.next:
                    list_result += f'{current.value} '
                    current = current.next
                else:
                    list_result += f'{current.value} '
                    return list_result
            except:
                print('Unexpected error')
                raise
        
    def append(self, value):
        new_node = Node(value)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def insert_before(self, key, value):
        new_node = Node(value)
        current = self.head

        if current.value == key:
            new_node.next = self.head
            self.head = new_node

        if self.head != key:
            if current.next:
                while current.next.value != key:
                    current = current.next
            new_node.next = current.next
            current.next = new_node
        return ValueError

    
    def insert_after(self, key, value):
        new_node = Node(value)
        current = self.head

        while current.value != key:
            if current.next:
                current = current.next
            else:
                break
        
        if current.value == key:
            new_node.next = current.next
            current.next = new_node
           
    def ll_merge(self, list2):
        head1 = self.head
        head2 = self.head
        if not head1 and not head2:
            return 'empty linked list'
        if head1 and not head2:
            return head1
        if not head1 and head2:
            return head2
        if head1 and head2:
            curr1 = head1
            curr2 = head2
            while curr1._next is not None and curr2._next is not None:
                ref1 = curr1._next
                ref2 = curr2._next
                curr1._next = curr2
                curr2._next = ref1
                curr1 = ref1
                curr2 = ref2
            if curr1._next is None and curr2:
                curr1._next = curr2
                return head1
            if curr2._next is None and curr1:
                ref1 = curr1._next
                curr1.next = curr2
                curr2.next = ref1
                return head1
        
    def kth_from_end(self, k):
        current = self.head

        if current:
            count_length = 0 

            while current.next != None:
<<<<<<< HEAD
                if current.next == None:
                    k = current.value
                    return current.value
                elif current.next != None:
                    current = current.next
            return ValueError

    def merge_lists(self, list_a, list_b):
        current = list_a.head
        a_curr = list_a.head
        b_curr = list_b.head

        while a_curr and b_curr:
            current.next = b_curr
            b_curr = b_curr.next
            current = current.next
            current.next = a_curr
            current = current.next

        return current

=======
                count_length += 1
                current = current.next

            n = count_length - k
            counter_two = 0
            current = self.head

            while counter_two < n:
                counter_two += 1
                current = current.next

            return current.value
        return None
>>>>>>> 4716f618a9e7ad5e39f930445dcb3739cfb897b7

class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


