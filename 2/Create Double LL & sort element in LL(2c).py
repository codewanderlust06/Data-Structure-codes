class Node:
    def __init__(self, info):
        self.info = info
        self.prev =None
        self.next = None

class DLL:
    def __init__(self):
        self.size =0
        self.head = None
        self.tail = None

    def insertatend(self, info):
        newnode = Node(info)
        if self.size == 0:
            self.head = newnode
            self.tail = newnode
            self.size+=1
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
            self.size+=1
        print("Node", info,"inserted successfully at the end of LL")

    def displayfromStart(self):
        ptr = self.head
        if ptr == None:
            print("LL is empty")
        else:
            while(ptr!=None):
                print(ptr.info)
                ptr = ptr.next
        print("Size of LL is",self.size)

            
    def displayfromend(self):
        ptr = self.tail
        if ptr == None:
            print("LL is empty")
        while(ptr!=None):
            print(ptr.info)
            ptr = ptr.prev
        print("Size of LL is",self.size)

    
    def bubbsort(self):
        for i in range(self.size-1):#for controlling passes of Bubble Sort
            currNode=self.head
            nxtNode=currNode.next
            prevNode=None
            while nxtNode:#Comparisons in passes
                if currNode.info>nxtNode.info:
                    if prevNode==None:
                       prevNode=currNode.next
                       nxtNode=nxtNode.next
                       prevNode.next=currNode
                       currNode.next=nxtNode
                       self.head=prevNode
                    else:   
                        tempNode=nxtNode
                        nxtNode=nxtNode.next
                        prevNode.next=currNode.next
                        prevNode=tempNode
                        tempNode.next=currNode
                        currNode.next=nxtNode
                else:           
                    prevNode=currNode
                    currNode=nxtNode
                    nxtNode=nxtNode.next
            i=i+1             

x = DLL()
x. displayfromStart()
x.insertatend(51)
x.insertatend(21)
x.insertatend(2)
x.insertatend(6)
x.insertatend(61)
x.insertatend(0)
x.displayfromStart()
print("Traversing from end")
x.displayfromend()

print("applying sorting")

x.bubbsort()
x.displayfromStart()
