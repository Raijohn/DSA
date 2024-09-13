class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
#lpr
def in_order_traversal(root):
    if root.left != None:
        in_order_traversal(root.left)
    print(root.key)
    if root.right != None:
        in_order_traversal(root.right)

#plr
def pre_order_traversal(root):
    print(root.key)
    if root.left != None:
        pre_order_traversal(root.left)
    if root.right != None:
        pre_order_traversal(root.right)

#lrp
def post_order_traversal(root):
    if root.left != None:
        post_order_traversal(root.left)
    if root.right != None:
        post_order_traversal(root.right)
    print(root.key)

Root = Node(1)

Root.left = Node(2)
Root.right = Node(3)

Root.left.left = Node(4)
Root.left.right = Node(5)

Root.right.left = Node(6)
Root.right.right = Node(7)

pre_order_traversal(Root)
print(" ")
post_order_traversal(Root)
print(" ")
in_order_traversal(Root)
