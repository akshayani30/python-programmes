print("ak")
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

#inorder left,right,root
def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data,end=" ")
    in_order(node.right)
#preorder:root,left,right
def pre_order(node):
    if node is None:
        return
    print(node.data,end=" ") #2 3 5 4
    in_order(node.left)
    in_order(node.right)
def post_order(node):  #left right root
    if node is None:
        return
    in_order(node.left)
    in_order(node.right)
    print(node.data,end=" ")   # 5 3 4 2 
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

if __name__ =="__main__":

    root=Node(2)
    root.left=Node(3)
    root.right=Node(4)
    root.left.left=Node(5)
    root.left.right=Node(6)

    subRoot = Node(3)
    subRoot.left = Node(5)
    subRoot.right = Node(6)


    print("IN-ORDER DFS:",end='')
    in_order(root)
    print("\nPRE-ORDER DFS:",end='')
    pre_order(root)
    print("\nPOST-ORDER DFS:",end='')
    post_order(root)
    print("\n level order:",end=" ")
    bfs(root)
    






































































































