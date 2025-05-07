class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Treeinfo:
    def __init__(self,height,diameter):
        self.height=height
        self.diameter=diameter
def bfs(root):    #level order traversal
    count=0
    sum=0
    if root is None:
        return
    queue=[root]
    while queue:
        print()
        node=queue.pop(0)
        print(node.data, end=' ')
        sum+=node.data
        count+=1

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print("\n number of nodes:",count)   
    print("\nsum of nodes:",sum)
def height(root):
    
    if root is None:
        return 0 # Height of an empty tree

    left_height = height(root.left)  # Recursively calculate height of left subtree
    right_height = height(root.right)  # Recursively calculate height of right subtree

    return max(left_height,right_height) + 1  # Height of current node is max of left and right subtree heights, plus 1
def diameter(root):
    if root is None:
        return Treeinfo(0,0)
    leftTI=diameter(root.left)
    rightTI=diameter(root.right)
    myheight=max(leftTI.height,rightTI.height)+1

    diam1=leftTI.diameter
    diam2=rightTI.diameter
    diam3=leftTI.height+rightTI.height+1
    mydiam=max(diam1,diam2,diam3)
    return Treeinfo(myheight,mydiam)
def Diameter1(root):
    if root ==None:
        return 0
    diam1=Diameter1(root.left)
    diam2=Diameter1(root.right)
    diam3=height(root.left)+height(root.right)+1

    return max(diam1,diam2,diam3)


if __name__ =="__main__":

    root=Node(2)
    root.left=Node(3)
    root.right=Node(4)
    root.left.left=Node(5)
    root.left.right=Node(6)

    subRoot = Node(3)
    subRoot.left = Node(5)
    subRoot.right = Node(6)


    
    print("\n level order:",end=" ")
    bfs(root)
    tree_height=height(root)
    print("\nmax tree height:",tree_height)
    tree_info=diameter((root))
    print("height:",tree_info.height)
    print("diameter:",tree_info.diameter)
    Diameter=Diameter1(root)
    print("Diameter of a tree is :",Diameter)
    






















