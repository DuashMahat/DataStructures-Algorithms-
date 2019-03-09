class CircularQueue():
    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0


    def __eq__(self, other):
        """
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity:
            return False
        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False
        return self.head == other.head and self.tail == other.tail and self.size == other.size

    # -----------MODIFY BELOW--------------

    def __str__(self):
        """
        Prints the elements in the queue
        """
        return ','.join([str(self.data[(self.head + i) % self.capacity]) for i in range(self.size)])

    def is_empty(self):
        """
         Returns whether empty or not
         True if empty , false otherwise
        """
        return self.size == 0

    def __len__(self):
        """
        Returns the size of the queue
        """
        return self.size

    def first_value(self):
        """
        Returns the front of the queue
        """
        if self.size == 0:
            return None
        return self.data[self.head]
    def enqueue(self, val):
        """
          insert new element into the queue
            param val : the value to equeued into the queue
          No return
        """
        if self.size == self.capacity:
            raise ValueError('queue full')
        self.size += 1
        self.data[self.tail] = val
        self.tail = (self.tail + 1) % self.capacity
        self.grow()

    def dequeue(self):
        """ delete top element from the queue
          Return: the value at the top of the queue
        """
        if self.size == 0:
            return None
        self.size -= 1
        val = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.shrink()
        return val

    def grow(self):
        """
            Doubles the capacity of the queue immediately when capacity is reached to make room for new elements
            Moves the head to the front of the newly allocated list
        """
        if self.size != self.capacity:
            return
        j = 0
        newcapacity = self.capacity * 2
        data = [None] * newcapacity
        for i in range(self.size):
            data[j] = self.data[(self.head + i) % self.capacity]
            j += 1
        self.head = 0
        self.data = data
        self.tail = self.size
        self.capacity = newcapacity

    def shrink(self):
        """
            Halves the capacity of the queue if the size is 1/4 of the capacity
            Capacity should never go below 4
            Moves the head to the front of the newly allocated list
        """
        if (self.capacity <= 4) or (self.size * 4 != self.capacity):
            return
        j = 0
        newcapacity = int(self.capacity / 2)
        data = [None] * newcapacity
        for i in range(self.size):
            data[j] = self.data[(self.head + i) % self.capacity]
            j += 1
        self.head = 0
        self.data = data
        self.tail = self.size
        self.capacity = newcapacity
        
