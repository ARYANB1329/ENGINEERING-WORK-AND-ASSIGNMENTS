class Node:
    def __init__(self, data):  # Constructor for Node class
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):  # Constrctor for LinkedList class
        self.head = None


    def append(self, data):
        new_node = Node(data)
        # If head is empty
        if self.head is None:
            self.head = new_node
            return
        # If head is not empty
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node



    def print_list_reverse(self):
        if self.head is None:
            print("EMPTY LINKED LIST")
            return
        s = []
        cur = self.head
        while cur:

            s.append(cur.data)
            cur = cur.next

        while s:
            print(s.pop(),end = " ")


ll = LinkedList()  # Creating a linked list
size = int(input())



l = list(map(int, input().split()))
for i in l:
    ll.append(i)

ll.print_list_reverse()