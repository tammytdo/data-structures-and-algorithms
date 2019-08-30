# add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

# get: takes in the key and returns the value from the table.

# contains: takes in the key and returns a boolean, indicating if the key exists in the table already.

# hash: takes in an arbitrary key and returns an index in the collection.

from linked_list import LinkedList

class HashTable:
    def __init__(self):
        self.buckets = [LinkedList()] * 1024

    def hash(self, key):
        char_sum = sum([ord(char) for char in key])
        prime_number = 97
        index = char_sum * prime_number % len(self.buckets)

        return index

    def add(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]
        bucket.insert({'key':key, 'value':value})

    def get(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]

        # adapt linked list includes()???
        

    def contains(self, key):
        # adapt linked list includes()
        current = self.head

        while current:
            if current.value == key_value:
                return True
            if current.value != key_value:
    
                new_current = current.next
                current = new_current

        # return boolean
        return value


    def hash(self, key):
        # return index
        pass