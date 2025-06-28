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
    #print("None")
def insert_at_end(head,data):

    current=head
    while(current.next != None):
        current=current.next
    new_node=Node(data)

    current.next=new_node
    new_node.next=None
def insert_at_pos(head,pos,data):
    if pos==0:
        head=insert_at_beginning(head,data)
    current=head
    index=0
    while current is not None and index + 1 !=pos:
        index +=1
        current=current.next
    if current is not None:
        new_node=Node(data)
        new_node.next=current.next
        current.next=new_node
    else:
        print("position is not found")
def del_at_beg(head):
    if head is None:
        return head
    temp=head
    
    head=head.next
    print("deleted at beginning node data is",temp.data)
    del temp
    return head
def del_at_end(head):
    current=head
    while(current.next != None):
        temp1=current
        current=current.next
    temp1.next=None
    del current
    return 
def del_at_end2(head):
    current=head
    while(current.next.next !=None):
        current=current.next
    current.next=current.next.next
    return
def del_at_pos(head,pos):
    if head is None:
        print("ak")
        return 
    if pos==0:
        return del_at_beg(head)
    index=0
    current=head
    while current is not None and current.next is not None and index+1 !=pos:
        index +=1
        current=current.next
    if current is not None and current.next is not None:
        current.next=current.next.next
        
    else:
        print("invalid position")
    return head



head=None
#head=insert_at_beginning(head,4)
# head=insert_at_beginning(head,5)
# insert_at_end(head,3)
# insert_at_end(head,1)
# insert_at_pos(head,3,2)
# head=del_at_beg(head)
# del_at_end(head)
head=del_at_pos(head,0)
traverse(head)


