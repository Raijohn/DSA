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

def search(root,node_value):
    if root.key < node_value and root.right != None:
        return search(root.right,node_value)
    elif root.key > node_value and root.left != None:
        return search(root.left,node_value)    
    elif root.key == node_value:
        return True
    else:
        return False
    
def in_order_successor(node):
    successor = node.right
    while successor.left != None:
        successor = successor.left
    return successor

def delete(root,value):
    if root == None:
        return root
    if value > root.key:
        root.right = delete(root.right,value)
    elif value < root.key:
        root.left = delete(root.left,value)
    else:
        if root.left == None:
            return root.right
        if root.right == None:
            return root.left
        temp = in_order_successor(root)
        root.key = temp.key
        root.right = delete(root.right,temp.key)
    return root


tree = None

for i in range(7):
    value = int(input("wich value do you want to add "))
    tree = insert_Node(tree,value)
in_order_trivisal(tree)
print(search(tree,int(input("what do you wanna search "))))
delete(tree,int(input("what do you wanna delete ")))
in_order_trivisal(tree)
