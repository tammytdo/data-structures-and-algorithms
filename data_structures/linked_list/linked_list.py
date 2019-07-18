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

    def kth_from_end(self, k, value):
        new_node = Node(value)
        current = self.head

        if current:
            while current.next != None:
                if current.next == None:
                    k = current.value
                    return current.value
                elif current.next != None:
                    current = current.next
            return ValueError
                
            
    def kth_from_end(self, k):
        

         basic_counter = 0	        basic_counter = 0
        length = 1	        length = 0
        current = self.head	        current = self.head


         while current.next:	        while current.next:
            length += 1	            length += 1
            current = current.next	            current = current.next


         k_endpoint = (length - k)	        k_endpoint = ((length + 1) - k)


         while basic_counter != k_endpoint:	        while basic_counter != k_endpoint:
            current = self.head	            current = self.head
            basic_counter += 1	            basic_counter += 1
            current = current.next	            current = current.next


         return current.next.node_value	        if k >= 1:
            return current.next.node_value
        elif k < 1:
            return self.head.node_value


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

class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


