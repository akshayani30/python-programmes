class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class circular_ll:
    def __init__(self):
        self.last=None
    
    def print_list(self):
        if self.last is None:
            return
        head=self.last.next
        while True:
            print(head.data,end="->")
            head=head.next
            if head==self.last.next:
                print("last")
                return
    def insert_at_beg(self,data):
        new_node=node(data)
        new_node.next=self.last.next
        self.last.next=new_node
        return
    def insert_at_end(self,data):
        new_node=node(data)
        new_node.next=self.last.next
        self.last.next=new_node
        self.last=new_node
        return
    def insert_at_pos(self,pos,data):
        if pos==0:
            return self.insert_at_beg(self,data)
            
        


    


