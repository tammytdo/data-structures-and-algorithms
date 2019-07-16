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
                 
class Node():
    def __init__(self, value, next):
        self.value = value
        self.next = next


