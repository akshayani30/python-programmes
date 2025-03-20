class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def print_list(last):   #same as singly list head but in clicular we will write last in last position
    if last is None:
        return 
    head=last.next
    while True:
        print(head.data,end="->")
        head=head.next
        if head==last.next:
            print("last")
            return
    
def insert_at_beg(data):
    #curr=last.next
    new_node=Node(data)
    new_node.next=last.next
    last.next=new_node
    return last
def insert_at_end(data):
    curr=last
    new_node=Node(data)
    new_node.next=curr.next
    curr.next=new_node
    curr=new_node
    return curr
def insert_at_pos(last,pos,data):
    if pos == 0:
        return insert_at_beg(data)
 #Create a new node with the given data
    new_node = Node(data)

    # curr will point to head initially
    curr = last.next

    # if pos == 0:
    #     # Insert at the beginning
    #     new_node.next = curr
    #     last.next = new_node
    #     return last

    # Traverse the list to find the insertion point
    for i in range(1, pos):
        curr = curr.next

        # If position is out of bounds
        if curr == last.next:
            print("Invalid position!")
            return last

    # Insert the new node at the desired position
    new_node.next = curr.next
    curr.next = new_node

    # Update last if the new node is inserted at the end
    if curr == last:
        last = new_node

    return last
  

def del_at_beg(last):
    if last is None:
        print("empty linked list")
        return None
    curr=last.next
    if curr == last:
        last = None
    else:
        last.next=curr.next
    return last
def del_at_end(last):
    curr=last.next

    while(curr.next !=last):
        curr=curr.next
    curr.next=last.next
    return curr
def del_at_pos(pos,last):
    if pos == 0:
        return del_at_beg
    curr=last.next
    for i in range(1,pos):
        curr=curr.next
        if curr  == last:
            print("invalid ")
            return last
    curr.next=curr.next.next
    return last
# def insertAtPosition(last, data, pos):
#     if last is None:
#         # If the list is empty
#         if pos != 1:
#             print("Invalid position!")
#             return last
#         # Create a new node and make it point to itself
#         new_node = Node(data)
#         last = new_node
#         last.next = last
#         return last

#     # Create a new node with the given data
#     new_node = Node(data)

#     # curr will point to head initially
#     curr = last.next

#     if pos == 1:
#         # Insert at the beginning
#         new_node.next = curr
#         last.next = new_node
#         return last

#     # Traverse the list to find the insertion point
#     for i in range(1, pos - 1):
#         curr = curr.next

#         # If position is out of bounds
#         if curr == last.next:
#             print("Invalid position!")
#             return last

#     # Insert the new node at the desired position
#     new_node.next = curr.next
#     curr.next = new_node

#     # Update last if the new node is inserted at the end
#     if curr == last:
#         last = new_node

#     return last

# # Function to print the circular linked list
# def print_list(last):
#     if last is None:
#         return

#     head = last.next
#     while True:
#         print(head.data, end="->")
#         head = head.next
#         if head == last.next:
#             break
#     print("last")



first=Node(2)
first.next=Node(3)
first.next.next=Node(4)
first.next.next.next=Node(5)
last=first.next.next.next
last.next=first
#last=insertAtPosition(last, 7, 0)

last=insert_at_beg(1)
last=insert_at_end(6)
last=insert_at_pos(last,6,7)
#last=del_at_beg(last)
#last=del_at_end(last)
last=del_at_pos(6,last)

print_list(last)




