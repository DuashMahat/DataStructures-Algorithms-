class HashNode:
    """
    DO NOT EDIT
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __repr__(self):
        return f"HashNode({self.key}, {self.value})"

class HashTable:
    """
    Hash table class, utilizes double hashing for conflicts
    """

    def __init__(self, capacity=4):
        """
        DO NOT EDIT
        Initializes hash table
        :param tableSize: size of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None]*capacity


    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True


    def __repr__(self):
        return '\n'.join(['[{}] {}'.format(i, str(self.table[i])) for i in range(len(self.table))])


    def hash_function(self, x):
        """
        ---DO NOT EDIT---

        Converts a string x into a bin number for our hash table
        :param x: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if x is an empty string
        """
        if not x:
            return -1
        hashed_value = 0

        for char in x:
            hashed_value = 181 * hashed_value + ord(char)

        return hashed_value % self.capacity


    def insert(self, key, value):
        """
        Inserts key(string) and value(string) into the HashTable using a HashNode
        param1 : key (string)
        param2 : value (string)
        return : None
        """
        if self.size / self.capacity > 0.75:
            self.grow()
        pos = self.quadratic_probe(key)
        if pos == -1:
            return
        if not self.table[pos]:
            self.size += 1
        self.table[pos] = HashNode(key, value)

    def quadratic_probe(self, key):
        """
        Runs the quadratic hashing procedure
        param1 : key (string)
        return : the table index of key if key is in the table
        """
        pos = self.hash_function(key)
        if pos == -1:
            return -1
        i = 1
        j = 1
        last_empty = -1
        while i <= self.capacity:
            if self.table[pos] and self.table[pos].key == key:
                return pos
            if (not self.table[pos]) and (last_empty == -1):
                last_empty = pos
            pos = (pos + j) % self.capacity
            i += 1
            j = i ** 2
        return last_empty

    def find(self, key):
        """
        Takes in a key to search for in the Hash Table
        param1 : key (string)
        Return:  the node with the given key if found, if not found it returns False
        """
        pos = self.quadratic_probe(key)
        if (pos == -1) or (not self.table[pos]) or (self.table[pos].key != key):
            return None
        return self.table[pos]

    def lookup(self, key):
        """
        Takes in a key to search for in the Hash Table
        param1 : key (string)
        Return:  the value of the node with the given key if found, if not found it returns False
        """
        node = self.find(key)
        if node:
            return node.value
        return False

    def delete(self, key):
        """
        Takes in a key to delete in the Hash Table
        param1 : string(key)
        Deletes by setting node to False
        Return : None
        """
        pos = self.quadratic_probe(key)
        if (pos == -1) or (not self.table[pos]) or (self.table[pos].key != key):
            return
        self.size -= 1
        self.table[pos] = None

    def grow(self):
        """
        Doubles capacity
        Rehashes all items in table
        params : None
        return : None
        """
        self.table = self.table + [None] * self.capacity
        self.capacity *= 2
        self.rehash()

    def rehash(self):
        """
        rehashes all items inside of the table
        params: None
        Return: None
        """
        old_table = self.table
        self.size = 0
        self.table = [None] * self.capacity
        for node in old_table:
            if not node:
                continue
            self.insert(node.key, node.value)

def string_difference(string1, string2):
    """
    Takes in two strings, uses hash tables to get the difference of characters from the strings
    param1 : string1 (string)
    param2 :string2 (string)
    Return: a set of the different characters, grouped by character
    """
    m = HashTable()
    for ch in string1:
        m.insert(ch, int(m.lookup(ch)) + 1)
    for ch in string2:
        m.insert(ch, int(m.lookup(ch)) - 1)
    n = set()
    for node in m.table:
        if node and node.value != 0:
            n.add(node.key * abs(node.value))
    return n
    
