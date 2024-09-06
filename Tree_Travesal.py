class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def in_order_traversal(root):
    while root.left != None:
        in_order_traversal(root.left)
    print(root.key)
    while root.right != None:
        in_order_traversal(root.right)

Root = Node(1)

Root.left = Node(2)
Root.right = Node(3)

Root.left.left = Node(4)
Root.left.right = Node(5)

Root.right.left = Node(6)
Root.right.right = Node(7)

in_order_traversal(Root)