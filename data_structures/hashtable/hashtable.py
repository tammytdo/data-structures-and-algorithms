from linkedlist import LinkedList

class HashTable:
    
    def __init__(self):
        self.buckets = [LinkedList() for i in range(1024)]

    def hash(self, key):
        char_sum = sum([ord(char) for char in key])
        prime_num = 97
        index = char_sum * prime_num % len(self.buckets)

        return index

    def add(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]
        bucket.insert({'key': key, 'value': value})

    def get(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]

        current = bucket.head

        while current:
            if current.value['key'] == key:
                return current.value['value']
            current = current.next

        raise ValueError

    def contains(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        current = bucket.head

        while current:
            if current.value['key'] == key:
                return True
            current = current.next

        return False