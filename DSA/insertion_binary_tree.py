from collections import deque   #deque from python collection module
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,key):
    if root is None:
        return Node(key)
    queue=deque([root])
    while queue:
        temp=queue.popleft()  #popleft() also same like pop(0)
        if temp.left is None:
            temp.left=Node(key)
            break
        else:
            queue.append(temp.left)
        
        if temp.right is None:
            temp.right=Node(key)
            break
        else:
            queue.append(temp.right)
    return root

        
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

# Function to search for a value in the binary tree using DFS
def searchDFS(root, value):
    # Base case: If the tree is empty or we've reached a leaf node
    if root is None:
        return False
    # If the node's data is equal to the value we are searching for
    if root.data == value:
        return True
    # Recursively search in the left and right subtrees
    left_res = searchDFS(root.left, value)
    right_res = searchDFS(root.right, value)

    return left_res or right_res
def deletion(root,val):
    if root is None:
        return None
    queue=deque([root])
    target=None
    while queue:
        curr=queue.popleft()
        if curr.data==val:
            target=curr
            break
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    if target is None:
        return root
    last_node=None
    last_parent=None
    queue=deque([(root,None)])
    while queue:
        curr,parent=queue.popleft()
        last_node=curr
        last_parent=parent

        if curr.left:
            queue.append((curr.left,curr))
        if curr.right:
            queue.append((curr.right,curr))
    target.data=last_node.data  #replace target data with last node data

    #remove the last node
    if last_parent:
        if last_parent.left==last_node:  #checking if there is only left node
            last_parent.left=None  
        else:
            last_parent.right = None  #if there is leftnode then right node is none
    else:
        return None
    return root

def bfs(root):
    if root is None:
        return
    queue=[root]
    while queue:
        level_size=len(queue)
        for _ in range(level_size):
            node=queue.pop(0)
            print(node.data,end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()
def print_level(root,k):
    if root is None:
        return
    if k < 0:
        print("Invalid level. Level should be >= 0")
        return      
    count=0
    sum=0
    queue=[root]
    while queue:
        level_size=len(queue)
        for _ in range(level_size):
            node=queue.pop(0)
            if count == k:
                sum += int(node.data)
                # print(node.data,end=" ")
                
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        count=count+1
        print()
    print("sum:",sum)

if __name__ == "__main__":
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)

    print("Inorder traversal before insertion: ", end="")
    inorder(root)
    print()


    root = insert(root, '6')

    print("Inorder traversal after insertion: ", end="")
    inorder(root)
    print()
    val=2
    if searchDFS(root,val):
        print(f"{val} is found in the binary tree")
    else:
        print(f"{val} is not found in binary tree")
    val_to_del=3
    root=deletion(root,val_to_del)
    # print(f"tree after deleting {val_to_del}(in-order):", end=" ")
    print("inorder traversal after deletion")
    inorder(root)
    print()
    bfs(root)  #it print level by level
    print_level(root,2)