def enqueue():
    if len(queue)==size:
        print("queue is full!!")
    else:
        element=input("enter the element:")
        queue.append(element)
        print(element,"is added to the queue!")
def dequeue():
    if len(queue)==0:
        print("queue is empty!!")
    else:
        print(queue[0],"element is removed!!")
        del queue[0]
        
        # print()
def display():
    if len(queue)==0:
        print("queue is empty!!")
    else:
        print("elements of the queue are")
        for element in queue:
            print(element,end=" ")
        print("\n front of the queue is",queue[0])
        print("\n front of the queue is",queue[-1])
size=int(input("enter the size of the queue:"))
queue=list()
while(1):
    print("select the operator:1.add 2.delete 3.display")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    else:
        print("invalid choice")

