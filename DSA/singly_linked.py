class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert_at_beginning(head,data):
    new_node=Node(data)
    new_node.next=head
    return new_node
def traverse(head):
    current=head
    while current:
        print(str(current.data) ,end="-> ")
        current=current.next
    print("None")
head=None
head=insert_at_beginning(head,4)
#head=insert_at_beginning(head,5)


traverse(head)
