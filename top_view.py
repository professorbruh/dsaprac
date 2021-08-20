class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def get_vertical_order(root,hd,m):
    if root == None:
        return
    try:
        m[hd].append(root.key)
    except:
        m[hd] = [root.key]

    get_vertical_order(root.left,hd-1,m)
    get_vertical_order(root.right,hd+1,m)

def print_vertical_order(root):
    hd = 0
    m = {}
    get_vertical_order(root,hd,m)
    for i in m:
        print(m[i][0])
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)
print_vertical_order(root)