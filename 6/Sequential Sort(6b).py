class ArrayOperations:
    def createArray(self):
        arr = []
        n = int(input("Enter the size of the array = "))
        for i in range(0,n):
            print("Enter the element at position", i)
            element = int(input())
            arr.append(element)
        print("array is:", arr)
        return arr
    
    def searchArray(self, arr):
        n = len(arr)
        item = int(input("Enter the element to be searched = "))
        for i in range(0,n):
            if arr[i] == item:
                pos = i
                print("Element", item, "found at position",pos)
                return pos
            
        print("Element", item, "not found in array")
        return -1
x = ArrayOperations()
array = x.createArray()
search = x.searchArray(array)


