class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def popfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp     

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        new_node = Node(value)
        temp = self.get(index)
        temp.next = new_node
        new_node.next = temp.next.next
        
    
print("Creating Linked List")
my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.printlist()


my_linked_list.insert(3,4)

my_linked_list.printlist()

my_linked_list.insert(1,7)

my_linked_list.printlist()

"""
print("set value function")
my_linked_list.set_value(2,7)
"""

"""
print("Get function being used")
print(my_linked_list.get_number(0))
print(my_linked_list.get_number(1))
print(my_linked_list.get_number(2))
print(my_linked_list.get_number(3))
"""
"""
print("pop First: ")
print(my_linked_list.popfirst())

print(my_linked_list.popfirst())

print(my_linked_list.popfirst())

print(my_linked_list.popfirst())

print(my_linked_list.popfirst())

print("Printing: ")
my_linked_list.printlist()

"""

"""
#print(my_linked_list.pop())

print(my_linked_list.pop())"""