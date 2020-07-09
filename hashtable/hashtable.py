class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        self.data = [None] * capacity
        self.count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """

        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # Hash index creates the index value based on the key
        index = self.hash_index(key)
        # create new LL item
        hst = HashTableEntry(key, value)
        # find this position in index
        node = self.data[index]
        # if the node exists already, we need to traverse the list
        # and check the next node.
        if node is not None:
            self.data[index] = hst
            self.data[index].next = node
        # Otherwise we need to put the thing here.
        else:
            self.data[index] = hst

        # while node is not null, if you come across a node with the same key just change the value with the new value otherwise check the next node, once it reaches the end add the new node
        # index = self.hash_index(key)
        # hst = HashTableEntry(key, value)
        # node = self.data[index]

        # if node is None:
        #     self.data[index] = hst
        # else:
        #     cur = self.data[index]
        #     while cur:
        #         if cur.key == key:
        #             cur.value = value
        #         elif cur.next:
        #             cur = cur.next
        #         else:
        #             break
        #         cur.next = hst

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        node = self.data[index]
        prev = None
        if node.key == key:
            self.data[index] = node.next
            return
        while node != None:
            if node.key == key:
                prev.next = node.next
                self.data[index].next = None
                return
            prev = node
            node = node.next
        return

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        node = self.data[index]
        if node is not None:
            while node:
                if node.key == key:
                    return node.value
                node = node.next
        return node

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        new_ht = HashTable(new_capacity)
        for entry in self.data:
            if entry:
                new_ht.put(entry.key, entry.value)
                if entry.next:
                    current = entry
                    while current.next:
                        current = current.next
                        new_ht.put(current.key, current.value)
        self.data = new_ht.data
        self.capacity = new_ht.capacity

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
