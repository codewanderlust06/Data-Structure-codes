class ArrayOperations:
    def createArray(self):
        arr = []
        n = int(input("Enter the size of the array"))
        for i in range(0,n):
            print("\n enter the element at position", i)
            element = int(input())
            arr.append(element)
        print("array is : ", arr)
        return arr

    def sortArray(self,arr):
        n=len(arr)
        for p in range(0,n-1):
            for s in range(0,n-p-1):
                if arr[s]>arr[s+1]:
                    temp = arr[s]
                    arr[s] = arr[s+1]
                    arr[s+1] = temp
        print("\n Sorted array using bubble sort is : ", arr)
        return arr

array=ArrayOperations()
myarray=array.createArray()
array.sortArray(myarray)




