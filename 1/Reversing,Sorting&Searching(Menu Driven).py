class ArrayOperations:
    def createArray(self):
        arr=[]
        n=int(input("Enter the size of the array:"))
        for i in range(0, n):
            print ("Enter the element at position:", i)
            element=int(input ())
            arr. append (element)
        print("Array is:",arr)
        return arr
    def reverseArray (self,arr):
        n=len(arr)
        i=0
        while(i<n):
            temp=arr [i]
            arr[i]=arr[n-1]
            arr[n-1]=temp
            i=i+1
            n=n-1
        print("Reversed Array is:",arr)
        return arr
    def sortArray(self, arr):
        n=len(arr)
        for p in range(0, n-1):
            for s in range (0, n-p-1):
                if arr[s]>arr[s+1]:
                    temp=arr[s]
                    arr[s]=arr[s+1]
                    arr[s+1]=temp
        print("Sorted array is:",arr)
        return arr
    def searchArray(self, arr):
        n=len(arr)
        item=int(input("Enter the element to be searched:"))
        for i in range (0, n):
            if arr[i]==item:
                pos=i
                print("Element",item,"found at position",pos)
                return pos
        print("Element is not found")
        return -1
array=ArrayOperations ()
myarray=array.createArray()
print("Menu\n")
print("1.Reversing 2.Sorting 3.Searching")
choice =int(input ("Enter your choice:"))
while choice!=4:
    if choice==1:
        array.reverseArray(myarray)
        exit()
    if choice==2:
        array.sortArray(myarray)
        exit()
    if choice==3:
        array.searchArray(myarray)
        exit()
