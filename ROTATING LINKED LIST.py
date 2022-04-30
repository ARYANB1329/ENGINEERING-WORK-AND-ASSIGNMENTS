#ARYAN SIDDHABATHULA 121910313029
#B13 29


class Node:
    def __init__(self):
        self.data = 0
        self.next = None
def rotate(head_ref, k):
    if (k == 0):
        return
    current = head_ref
    while (current.next != None):
        current = current.next
    current.next = head_ref
    current = head_ref
    for i in range(k - 1):
        current = current.next
    head_ref = current.next
    current.next = None
    return head_ref
def push(head_ref, new_data):
    new_node = Node()
    new_node.data = new_data
    new_node.next = (head_ref)
    (head_ref) = new_node
    return head_ref
def printList(node):
    while (node != None):
        print(node.data, end = ' ')
        node = node.next
if __name__=='__main__':
    head = None
    for i in range(7, 0, -1):
        head = push(head, i)
    head = rotate(head, 4)
    print("\nRotated Linked list ")
    printList(head)