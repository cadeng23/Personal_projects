
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

root = Node('Caden')

root.left = Node(0)
root.right = Node(1)
root.left.left = Node(0)
root.left.right = Node(1)

def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

preorder(root)