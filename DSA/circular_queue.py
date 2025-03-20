class Circularqueue:
    def __init__(self,size):
        self.maxsize=size
        self.queueArray=[0]*size
        self.front=-1
        self.rear=-1
    def enqueue(self,item):
        if self.isEmpty():
            self.front=0
            self.rear=0
            self.queueArray[self.rear]=item
        else:
            self.rear=(self.rear+1) % self.maxsize
            if self.rear==self.front:
                print("queue is full. Cannot enqueue.")
                self.rear=(self.rear-1 +self.maxsize)%self.maxsize
            else:
                self.queueArray[self.rear]=item
    
    def dequeue(self):
        item=-1 
        if not self.isEmpty():
            item=self.queueArray[self.front]
            self.queueArray[self.front]=None
            if self.front == self.rear:
                self.front=-1
                self.rear=-1

            else:
                self.front=(self.front +1)%self.maxsize
        else:
            print("queue is empty.Canot dequeue.")

        return item
    def peek(self):
        if not self.isEmpty():
            return self.queueArray[self.front]
        else:
            print("queue is empty. No peek value.")
            return -1
    def isEmpty(self):
        return self.front==-1 and self.rear ==-1    
    
circular_queue=Circularqueue(5)
circular_queue.enqueue(1)
circular_queue.enqueue(2)
circular_queue.enqueue(3)
circular_queue.enqueue(4)
circular_queue.enqueue(5)
circular_queue.enqueue(1)
print(circular_queue.queueArray)

print("peek:",circular_queue.peek())
circular_queue.dequeue()
print(circular_queue.queueArray)


        
