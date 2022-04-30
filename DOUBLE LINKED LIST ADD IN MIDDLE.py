# Program to add a node at the middle of a Doubly Linked List
# ARYAN SIDH 121910313029

# Defining the Node class
class Node:
    def __init__(self, data):  # Constructor for Node class
        self.data = data
        self.prev = None
        self.next = None


# Definind the Doubly Linked List Class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Method to append new nodes
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur

    # Method to Print Nodes of Linked List
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next

    # Method to Update Head
    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Method to insert at middle
    def add_at_middle(self, key, data):
        new_node = Node(data)
        cur = self.head
        while cur.next:
            nxt = cur.next
            if cur.data == key:
                cur.next = new_node
                new_node.prev = cur
                new_node.next = nxt
                nxt.prev = new_node
            cur = cur.next


dll = DoublyLinkedList()
n = int(input("Enter the size of the linked list : "))
print("Enter the elements of the linked list")
for i in range(n):
    dll.append(input())

print("The old linked list : ")
dll.print_list()
print()
k = input("Enter the node after which we should add the node : ")
h = input("Enter the new node : ")
dll.add_at_middle(k, h)
print("The updated linked list is : ")
dll.print_list()
