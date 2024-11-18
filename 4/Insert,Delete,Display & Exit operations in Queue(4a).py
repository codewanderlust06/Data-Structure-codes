class Node:
    def __init__(self,info):
        self.info = info
        self.next = None
class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    def Enqueue(self,info):
        newnode = Node(info)
        if self.size == 0:
            self.front = newnode
            self.rear = newnode
            self.size+=1
        else:
            self.rear.next = newnode
            self.rear = newnode
            self.size+=1
        print("Element",info,"inserted successfully in the queue")
    def Dequeue(self):
        if self.size ==0:
            print("Queue is empty")
        else:
            value = self.front.info
            if self.size == 1:
                self.front = None
                self.rear = None
                self.size-=1
            else:
                self.front = self.front.next
                self.size-=1
            print("The deleted value is : ",value)
            return value
    def Display(self):
        if self.size == 0:
            print("Queue is empty")
        else:
            ptr = self.front
            while(ptr!=None):
                print(ptr.info)
                ptr=ptr.next
            print("The size of the queue is : ",self.size)
q=QueueLL()
q.Display()
q.Enqueue(5)
q.Enqueue(51)
q.Display()
q.Dequeue()
q.Display()
q.Dequeue()
q.Display()



