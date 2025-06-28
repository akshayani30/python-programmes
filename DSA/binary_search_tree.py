class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Binary_search:
    def __init__(self):
        self.root = None
    def insert(self,root,data):
        if root is None:
            return Node(data)
        if data<root.data:
            root.left=self.insert(root.left,data)
        if data>root.data:
            root.right=self.insert(root.right,data)
        
        return root  #return the unchanged root
    def find_min(self,root):  #to find the node with min value
        while root.left is not None:
            root=root.left  #go as far left as possible bcz at left min value will be there
            
            return root
    def delete(self,root,data):
        if root is None:
            return root  #base case tree is empty returns None
        if data<root.data:
            root.left=self.delete(root.left,data)
        elif data > root.data:
            root.right=self.delete(root.right,data)
        else:
            #case 1: Node has no left child
            if root.left is None:
                temp=root.right
                root=None
                return temp
            #case 2:Node has no right child
            elif root.right is None:
                temp=root.right
                root=None
                return temp
            #case 3: Node has two children
            #inorder successor smallest in the right sub tree or we can also do highest in the left sub tree
            temp=self.find_min(root.right)
            root.data=temp.data  #replace root data with smallest data in right sub tree
            root.right=self.delete(root.right,temp.data)  #delete the smallest data None
            return root
            

        