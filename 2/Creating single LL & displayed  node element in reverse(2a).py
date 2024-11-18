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

    
    def reverseLL(self):
        ptr = self.begin
        if ptr==None:
            print("Linked list is empty")

        if ptr.next ==None:
            print("Linked list has only one element, cant reverse")

        if ptr.next is not None:
            ptr1 = ptr
            ptr2 = ptr.next
            ptr3 = ptr2.next

        if ptr3 ==None:
            ptr2.next = ptr1
            ptr1.next = None
            self.begin = ptr2
        ptr1.next=None
        while(ptr3.next !=None):
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2=ptr3
            ptr3 = ptr3.next

        ptr2.next = ptr1
        ptr3.next = ptr2
        self.begin = ptr3
        
x=LinkedList()
x.insertbeg(50)
x.insertbeg(40)
x.insertbeg(30)
x.insertbeg(20)
x.insertbeg(500)
x.insertbeg(10)
x.insertbeg(360)
x.insertbeg(250)
x.displayLL()

x.reverseLL()
print("Printing reversed Linked list:")
x.displayLL()
