class Node():
      def __init__(self, info):
        self.info = info
        self.next = None
     
class Stack():
    def __init__(self):
        self.top=None
        self.size=0
 
    def push(self, info):
        newnode=Node(info)
        newnode.next = self.top
        self.top = newnode
        self.size+=1
 
    def pop(self):
        if(self.top == None):
            print("Stack is empty")
        else:
            value = self.top.info
            self.top = self.top.next
            self.size-=1
            print("The element popped is", value)
        
        
    def display(self):
        if self.top==None:
            print("Stack is Empty")
        else:
            self.temp = self.top
            while(self.temp !=None):
                print(self.temp.info)
                self.temp = self.temp.next
        print("Size of stack is",self.size)
 
s = Stack()
s.display()
s.push(3)
s.push(5)
s.push(9)
s.push(7)
s.display()
s.pop()
s.display()
