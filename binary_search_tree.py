class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

#lpr
def in_order_trivisal(root):
    if root.left != None:
        in_order_trivisal(root.left)
    print(root.key)
    if root.right != None:
        in_order_trivisal(root.right)

def insert_Node(root,new):
    if root == None:
        return Node(new)
    if root.key < new:
        root.right = insert_Node(root.right,new)
    else:
        root.left = insert_Node(root.left,new)
    return root

tree = None

for i in range(7):
    value = int(input("wich value do you want to add "))
    tree = insert_Node(tree,value)
in_order_trivisal(tree)
