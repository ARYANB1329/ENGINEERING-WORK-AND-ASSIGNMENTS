# Represent a node of the singly linked list
class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;


class Remove:
    # Represent the head and tail of the singly linked list
    def __init__(self):
        self.head = None;
        self.tail = None;

        # addNode() will add a new node to the list

    def add(self, data):
        # Create a new node
        newNode = Node(data);

        # Checks if the list is empty
        if (self.head == None):
            # If list is empty, both head and tail will point to new node
            self.head = newNode;
            self.tail = newNode;
        else:
            # newNode will be added after tail such that tail's next will point to newNode
            self.tail.next = newNode;
            # newNode will become new tail of the list
            self.tail = newNode;

            # removeDuplicate() will remove duplicate nodes from the list

    def removeDup(self):
        # Node current will point to head
        current = self.head;
        index = None;
        temp = None;

        if (self.head == None):
            return;
        else:
            while (current != None):

                temp = current;

                index = current.next;

                while (index != None):

                    if (current.data == index.data):

                        temp.next = index.next;
                    else:

                        temp = index;
                    index = index.next;
                current = current.next;

    def disp(self):

        current = self.head;
        if (self.head == None):
            print("List is empty");
            return;
        while (current != None):
            print(current.data, end=" ");
            current = current.next;


ll = Remove();
n = int(input())
l = list(map(int, input().split()))
for i in l:
    ll.add(i)
ll.removeDup()
ll.disp()