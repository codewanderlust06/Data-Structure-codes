class ArrayOperation:
    def createArray(self):
        arr=[]
        n=int(input("Enter the size of the array = "))
        for i in range(0,n):

            print("Enter the element at position",i)
            element=int(input())

            arr.append(element)
        print("Array is : ",arr)
        return arr

    def searchArray(self,arr):
        n=len(arr)
        item=int(input("Enter the item to be searched"))
        for i in range(0,n):
            if arr[i]==item:
                pos=i
                print("Element",item,"is found at position",pos)
                return pos

        print("Element is not found")
        return -1

array=ArrayOperation()
myarray=array.createArray()
searchArray=array.searchArray(myarray)




    



            

            
