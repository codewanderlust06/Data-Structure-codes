class CQ:
 
    def __init__(self,maxsize): 
 
        self.queue = list() 
 
        self.maxsize = maxsize 
 
        self.front = 0 
 
        self.rear = 0 
 
 
 
    def EnqueueCQ(self, info): 
 
        if self.size() == self.maxsize-1: 
 
            print("queue is full")
        else:
 
            self.queue.append(info) 
 
            print("element",info , "inserted successfully at",self.rear)  
 
            self.rear = (self.rear + 1)% self.maxsize
            print("Total elements in queue are", self.size())
 
        return 1 
 
 
 
    def DequeueCQ(self): 
 
        if self.size() == 0: 
 
            print("queue is empty")
        else:
 
            value = self.queue[self.front] 
 
            print("element",value , "deleted successfully from",self.front) 
 
            self.front = (self.front + 1)% self.maxsize
        print("Total elements in queue are", self.size())
        return 1
 
  
 
    def size(self): 
 
        if self.rear >= self.front: 
 
            size = (self.rear - self.front) 
        else:
            size = (self.maxsize - (self.front - self.rear))
        return size 
 
 
size = input("Enter the size of the Circular Queue = ")
q = CQ(int(size))
 
 
 
q.EnqueueCQ(1) 
 
q.EnqueueCQ(2) 
 
q.EnqueueCQ(3) 
 
q.EnqueueCQ(4) 
 
q.EnqueueCQ(5) 
 
q.EnqueueCQ(12)
 
q.DequeueCQ()
q.DequeueCQ()
q.DequeueCQ()
q.DequeueCQ()
