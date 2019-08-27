# Hashtables
A hashtable allows the ability to store a key and quickly retrieve the value. A hash mean to encode the key so that it maps to a specific location in the data structure that we can look at directly to retrieve the value.

## Challenge
Implement a Hashtable with the following methods:

-add()
-get()
-contains()
-hash()

## Approach & Efficiency
The structure of this hashtable is a list. The key and value are stored as nodes in a linked list at the index of the hashed key. If another key hashes to the same value, another node is added to the linked list. 

## API
-add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

-get: takes in the key and returns the value from the table.

-contains: takes in the key and returns a boolean, indicating if the key exists in the table already.

-hash: takes in an arbitrary key and returns an index in the collection.