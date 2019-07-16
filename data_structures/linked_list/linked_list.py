class LinkedList():

    def __init__(self):
        self.head = None
    
    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, search_value):
        current = self.head
        if self.head == None:
            return False
        while current.next:
            if current.value == search_value:
                return True
            if current.value != search_value:
                current = current.next
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


