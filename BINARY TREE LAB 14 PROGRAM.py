class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,root):
        self.root = Node(root)

    def insert(self,val):
        node = Node(val)
        q = [self.root]
        while len(q)!=0:
            n = q.pop(0)
            if n.left == None:
                n.left = node
                break
            else:
                q.append(n.left)
                if n.right == None:
                    n.right = node
                    break
                else:
                    q.append(n.right)


tree = BinaryTree(100)
for i in range(11):
    tree.insert(i)
