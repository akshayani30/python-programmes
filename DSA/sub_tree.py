class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def is_identical(root, subRoot):
    
    if subRoot is None and root is None:
        return True
    if root is None or subRoot is None:
        return False
    if root.data == subRoot.data:
        return is_identical(root.left, subRoot.left) and is_identical(root.right, subRoot.right)
    return False

def is_subtree(root, subRoot):
    
    if subRoot is None:
        return True
    if root is None:
        return False
    if is_identical(root, subRoot):
        return True
    return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot)


if __name__ =="__main__":

    root=Node(2)
    root.left=Node(3)
    root.right=Node(4)
    root.left.left=Node(5)
    root.left.right=Node(6)

    subRoot = Node(3)
    subRoot.left = Node(5)
    subRoot.right = Node(6)

    
    # Check if subRoot is a subtree of root
    result = is_subtree(root, subRoot)
    if result:
        print("subRoot is a subtree of root")
    else:
        print("subRoot is not a subtree of root") 























