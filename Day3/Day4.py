# Create a Singly linked List.
# Section 1: Create Node Class
class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

#Section 2: Create the Linked List Class
class LinkedList :
    def __init__(self):
        self.head = None
        self.length = 0

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def insert_start(self, data): # Inserting New Node at the start of the List
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, data): # Inserting Node at the end of the list
        if self.head is None:
            self.head = Node(data)
            self.length += 1
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(data)
        self.length += 1


    def remove(self):
        if self.head is None:
            return None
        if self.head.next is None :
            self.head= None
            self.length -= 1
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        self.length -= 1

    def remove_start(self):
        if self.head is None:
            return None
        self.head = self.head.next
        self.length -= 1

    def insert_between(self,data,index):
        if index == 0 :
            self.remove_start()
        temp = self.head
        for i in range(index-1):
            temp = temp.next
        if temp is None:
            return
        newNode = Node(data)
        newNode.next = temp.next
        temp.next = newNode
        self.length += 1

l = LinkedList()
l.insert_start(1)
l.insert_start(2)
l.insert_start(3)
l.insert_start(4)
l.print_list()
l.insert_between(56,5)
l.print_list()