class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.head=None
        self.last=None
    def enqueue(self,data):
        if self.last is None:
            self.head=Node(data)
            self.last=self.head
        else:
            self.last.next=Node(data)
            self.last=self.last.next
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return=self.head.data
            self.head=self.head.next
            return to_return
    def display(self):
        if self.head is None:
            print("queue is empty")
            return
        current= self.head
        queue_ele=[]
        while current:
            queue_ele.append(str(current.data))
            current=current.next
        print("queue :"+"->".join(queue_ele))
a_queue=queue()
while True:
    print("queue operations")
    print("1.enqueue<value>")
    print("2.dequeue")
    print("3.quit")
    print("4.display")
    do=input('what would you like to do?').split()
    operation=do[0].strip().lower()
    if operation =="enqueue":
        a_queue.enqueue(int(do[1]))
    elif operation =='dequeue':
        dequeue=a_queue.dequeue()
        if dequeue is None:
                print("queue is empty")
        else:
                print("dequeue element:",int(dequeue))
    elif operation =="display":
        a_queue.display()
    elif operation == "quit":
        break
    else:
        print("invalid operation")
    