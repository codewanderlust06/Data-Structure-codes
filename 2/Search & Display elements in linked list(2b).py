class Node():
      def __init__(self, info):
        self.info = info
        self.next = None
     
class LinkedList():
    def __init__(self):
        self.begin=None
        #self.tail=None
        self.size=0
    
    def insertbeg(self, info):
        newnode=Node(info)
        if self.begin==None:
            self.begin=newnode
            #self.tail=None
        else:
            newnode.next=self.begin
            self.begin=newnode
        print("node inserted successfully with data",info,"at the beginning")
        self.size+=1
        
        
    def displayLL(self):
        if self.begin==None:
            print("Linked List is Empty")
        else:
            ptr = self.begin
            while(ptr!=None):
                print(ptr.info)
                ptr=ptr.next
            print('size of linked list is:',self.size)

    
    def searchLL(self, item):
        ptr = self.begin
        if ptr == None:
            print("Linked list is empty")
            
        while(ptr!=None):
            if(ptr.info == item):
                print("Item",item,"found at position",ptr)
                return ptr
            else:
                ptr = ptr.next
        print("Item",item,"Not found in the linked list")
        return -1





            

x=LinkedList()
x.insertbeg(50)
x.insertbeg(40)
x.insertbeg(30)
x.insertbeg(20)        
x.displayLL()
x.searchLL(20)
