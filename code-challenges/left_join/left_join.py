from hashtable import HashTable

def left_join(ht_1, ht_2):
    joined_list = []

    for i in range(len(ht_1.buckets)):
        if ht_1.buckets[i].head:
            ht_1_keys = []

            current = ht_1.buckets[i].head
            ht_1_keys.append(current.value['key'])
            ht_1_keys.append(current.value['value'])
            joined_list.append(ht_1_keys)

    for lst in joined_list:
        for first_word in lst:
            if ht_2.contains(first_word):
                lst.append(ht_2.get(first_word))
            
            if not ht_2.contains(first_word):
                lst.append('None')

    return joined_list

        



