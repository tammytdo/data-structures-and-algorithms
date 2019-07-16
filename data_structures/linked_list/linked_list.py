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

    def insert_before(self, key, insert_value):
        new_node = Node(insert_value)
        new_current = self.head

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

    
    def insert_after(self, key, insert_value):
        #define the new node
        new_node = Node(value)

        #define the head
        current = self.head

        #loop through nodes
        #while a value exists and is not equal to the key:
        while current.value != key:
            #if there is a next:
            if current.next:
                #set the new current to current.next
                current = current.next
            else:
                break
        
        if current.value == key:
            new_node.next = current.next
            current.next = new_node
    

class Node():
    def __init__(self, value, next):
        self.value = value
        self.next = next


