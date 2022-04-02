
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

# In order traversal recursion
def print_inorder_recursion(root):
    if root:
        print_inorder_recursion(root.left)

        print(root.data,end=" ")

        print_inorder_recursion(root.right)

# In order without recursion
def print_inorder_stack(root):
    stack=[]
    current = root

    while(True):
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current=stack.pop()
            print(current.data,end=" ")
            current = current.right
        else:
            break

# In order traversal recursion
def print_preorder_recursion(root):
    if root:
            
        print(root.data,end=" ")
           
        print_preorder_recursion(root.left)

        print_preorder_recursion(root.right)

# In order traversal recursion
def print_preorder_stack(root):
    current = root
    stack = []
    while True:
        if current is not None:
            stack.append(current)
            print(current.data,end=" ")
            current=current.left
        elif stack:
            current=stack.pop()
            current=current.right
        else:
            break

# Post order traversal
def print_postorder_recursion(root):
    if root:
        print_postorder_recursion(root.left)

        print_postorder_recursion(root.right)

        print(root.data, end=" ")

# post order traversal stack
def print_postorder_stack(root):
    current = root
    stack = []
    while True:
        if current is not None:
            stack.append(current)
            current=current.left
        elif stack:
            current=stack.pop()
            print(current.data,end=" ")
            current=current.right
            
            

        else:
            break

class __Main__:
    root=Node(5)

    root.left=Node(4)

    root.left.left=Node(2)

    root.left.right=Node(3)

    root.right=Node(6)

    root.right.left=Node(7)

    root.right.right=Node(8)

    print('\n',"In Order Recursion:")
    print_inorder_recursion(root)

    print('\n',"In Order Stack:")
    print_inorder_stack(root)


    print('\n',"Pre Order Recursion:")
    print_preorder_recursion(root)

    print('\n',"Pre Order Stack:")
    print_preorder_stack(root)

    print('\n',"Post Order Recursion:")
    print_postorder_recursion(root)

    print('\n',"Post Order Stack:")
    print_postorder_stack(root)

