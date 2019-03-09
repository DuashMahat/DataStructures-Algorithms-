class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'next_node'

    def __init__(self, value, next_node=None):
        """
        DO NOT EDIT
        Initialize a node
        :param value: value of the node
        :param next_node: pointer to the next node, default is None
        """
        self.value = value  # element at the node
        self.next_node = next_node  # reference to next node

    def __eq__(self, other):
        """
        DO NOT EDIT
        Determine if two nodes are equal (same value)
        :param other: node to compare to
        :return: True if nodes are equal, False otherwise
        """
        if other is None:
            return False
        if self.value == other.value:
            return True
        return False

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a node
        :return: string of value
        """
        return str(self.value)

   
class LinkedList:
    def __init__(self):
        """
        DO NOT EDIT
        Create/initialize an empty linked list
        """
        self.head = None   # Node
        self.tail = None   # Node
        self.size = 0      # Integer

    def __eq__(self, other):
        """
        DO NOT EDIT
        Defines "==" (equality) for two linked lists
        :param other: Linked list to compare to
        :return: True if equal, False otherwise
        """
        if self.size != other.size:
            return False
        if self.head != other.head or self.tail != other.tail:
            return False

        # Traverse through linked list and make sure all nodes are equal
        temp_self = self.head
        temp_other = other.head
        while temp_self is not None:
            if temp_self == temp_other:
                temp_self = temp_self.next_node
                temp_other = temp_other.next_node
            else:
                return False
        # Make sure other is not longer than self
        if temp_self is None and temp_other is None:
            return True
        return False

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a linked list
        :return: string of list of values
        """
        temp_node = self.head
        values = []
        if temp_node is None:
            return None
        while temp_node is not None:
            values.append(temp_node.value)
            temp_node = temp_node.next_node
        return str(values)

    ###### MODIFY THE BELOW FUNCTIONS #####

    # ------------------------Accessor Functions---------------------------

    def length(self):
        """
        Gets the number of nodes of the linked list
        :return: size of list
        """
        # count = 0
        # temp_linked_node = self.head
        # while temp_linked_node is not None:
        #   count+=1
        #   temp_linked_node = temp_linked_node .next_node
        # return count
        
        return self.size
    
    def is_empty(self):
        """
        Determines if the linked list is empty
        :return: True if list is empty and False if not empty
        """
        temp_linked_node2 = self.head
        if (temp_linked_node2 != None): 
             return False
        return True
        

    def front_value(self):
        """
        Gets the first value of the list
        :return: value of the list head
        """
        temp_linked_node3 = self.head

        if ( temp_linked_node3 != None):
           return temp_linked_node3.value


    def back_value(self):
        """
        Gets the last value of the list
        :return: value of the list tail
        """
        temp_linked_node4 = self.head
        temp_linked_node5 = self.head
        count2 = 0
        if (temp_linked_node4 != None): 
           while temp_linked_node4  is not None:
             count2+=1
             temp_linked_node4 = temp_linked_node4.next_node
        for i in range(count2 - 1):
           temp_linked_node5 = temp_linked_node5.next_node

        return  temp_linked_node5.value
        

            

    def count(self, val):
        """
        Counts the number of times a value 'val' occurs in the list
        :param val: value to find and count
        :return: number of time 'val' occurs
        """
        count = 0
        temp_linked_node10 = self.head
        while temp_linked_node10 is not None:
          if ( temp_linked_node10.value == val):
             count+=1
          temp_linked_node10  =  temp_linked_node10.next_node
        return count



        

    def find(self, val):
        """
        Searches for and returns the first node with the value 'val'
        :param val: value to search for
        :return: True if value is in list, False if value is not found
        """
        if self.size == 0:
          return None
        temp_linked_node11 =  self.head
        while temp_linked_node11 is not None:
          if  temp_linked_node11.value == val:
            # return temp_linked_node11 
            return True
          temp_linked_node11 = temp_linked_node11.next_node
        return False
        

            


    # ------------------------Mutator Functions---------------------------

    def push_front(self, val):
        """
        Adds a node to the front of the list with value 'val'
        :param val: value to add to list
        :return: no return
        """

        #  1-> 2 -> 3   4 
        if self.size == 0:
            #temp_linked_node_front = Node(val)
            self.head = Node(val)
            self.size+=1
            self.tail = self.head
            return
        if self.size > 0:
            temp_linked_node_front = Node(val , None)
            temp_linked_node_front.next_node = self.head
            self.head = temp_linked_node_front
            self.size+=1
            return
   
       
    def push_back(self, val):
        """
        Adds a node to the back of the list with value 'val'
        :param val: value to add to list
        :return: no return
        """
        # 1 -> 2 -> 3 -> 4 
        # if  self.head is None:
        #    temp_linked_nodeGetLastStart = Node(val , None)
        #    self.head = temp_linked_nodeGetLastStart
        #    temp_linked_nodeGetLastStart = self.tail
        #    self.size+=1
        # else:
        if self.size == 0:
            #temp_linked_node_front = Node(val)
            self.tail = Node(val)
            self.size+=1
            self.head = self.tail
            return
        
        
        temp_linked_nodeTail = Node(val , None)
        temp_linked_nodeGetLastStart = self.head
        for i in range(self.size - 1):
          temp_linked_nodeGetLastStart = temp_linked_nodeGetLastStart.next_node
        
        #self.tail = temp_linked_nodeGetLastStart
        self.tail.next_node = temp_linked_nodeTail
        # temp_linked_nodeTail = self.tail
        self.tail = self.tail.next_node
        self.size+=1
        

    def pop_front(self):
        """
        Removes a node from the front of the list
        :return: the value of the removed node
        """
        if self.size == 0:
          return None
        val = self.head.value
        self.head = self.head.next_node
        self.size-=1
        return val
        

    def pop_back(self):
        """
        Removes a node from the back of the list
        :return: the value of the removed node
        """
        temp_linked_node21 = self.tail
        temp_linked_node22 = self.head
        if (self.head.next_node is None):
           val = self.head.value
           self.head = None
           return val
           self.size-=1
        val2 = temp_linked_node21.value
        # self.head = self.head.next_node
        for i in range(self.size - 2):
            temp_linked_node22 = temp_linked_node22.next_node
        self.tail = temp_linked_node22
        self.tail.next_node = None
        self.size-=1;
        return val2


    def reverse_list(self):
        """
        Reverses the values of the given linked list
        :return: no return
        """
        temp_ptr = self.head
        temp_prev = None
        temp_temp = Node(0 , None)
        while temp_ptr is not None:
            temp_temp = temp_ptr.next_node
            temp_ptr.next_node = temp_prev
            temp_prev = temp_ptr
            temp_ptr = temp_temp
        self.head = temp_prev
