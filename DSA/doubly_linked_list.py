class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def insert_at_beg(data):
    new_node=Node(data)
    new_node.next=head
    if head:            #here  cheking the nodes are there are not
        head.prev=new_node
    new_node.prev=None   #not mentioning also no problem bcoz we mentioned in globally
    return new_node
def insert_at_end(data):
    new_node=Node(data)
    new_node.next=None
    current=head
    while current.next != None:
        current=current.next
    new_node.prev=current.next
    current.next=new_node
    return head
def insert_at_pos(pos,data):
   
    new_node=Node(data)
    current=head
    count=1
    if pos==0:
        return insert_at_beg(data)
    while count != pos:
        if current.next == None:      #count=1,2,3,4   curr=1,2,3,4
            print("invaid")
            return head
        current=current.next   
        
        if count == pos-1:    
            new_node.next=None
            new_node.prev=current
            current.next=new_node
            print("entered in if")
            return head
        
        count +=1
    new_node.next=current.next
    
    current.next.prev=new_node
    new_node.prev=current
    current.next=new_node
    return head
def del_at_beg(head):
    temp=head
    head=head.next
    del temp
    return head
def del_at_end(head):
    temp=head
    while temp.next != None:
        old_temp=temp
        temp=temp.next
    old_temp.next=None
    del temp
    return head
def del_at_pos(head,pos):
    current=head
    count=1
    if pos==0:
        return del_at_beg(head)
    while current.next:
        if count==pos:
            if current.next.next== None:  
                return del_at_end(head)
            current.next.next.prev=current
            current.next=current.next.next
                
            
            return head
        count+=1
        current=current.next
       
    print("invalid position")
    return head

def traverse(head):
    current=head
    while current:
        print(current.data,end= " <-> ")
        current=current.next
    print(" None")
head=None
head=insert_at_beg(3)
head=insert_at_beg(2)
head=insert_at_beg(1)
head=insert_at_end(4)
head=insert_at_pos(4,0)
traverse(head)
head=del_at_beg(head)
head=del_at_end(head)
head=del_at_pos(head,3)
traverse(head)

