class ArrayOperations:
    def createArray(self):
        arr = []
        n = int(input("Enter the size of the array : "))
        for i in range(0,n):
            print("Enter the element at position", i)
            element = int(input())
            arr.append(element)
        print("Array is:", arr)
        print(type(arr))
        return arr
    
    def mergeArray(self, arr1, arr2):
        
        output_arr = []
        n1 = len(arr1)
        n2 = len(arr2)
        
        lb1 = 0
        ub1 = n1-1
        
        lb2 = 0
        ub2 = n2-1
        while (lb1<n1 and lb2<n2):
            if arr1[lb1]>arr2[lb2]:
                element = arr2[lb2]
                output_arr.append(element)
                lb2=lb2+1
            else:
                element = arr1[lb1]
                output_arr.append(element)
                lb1=lb1+1
        if lb1 > ub1:
            while(lb2<n2): #or lb2<=ub2
                element = arr2[lb2]
                output_arr.append(element)
                lb2=lb2+1
        else:
            if lb2 > ub2:
                while(lb1<n1):
                    element = arr1[lb1]
                    output_arr.append(element)
                    lb1 = lb1+1
        print("Merged array is",output_arr)
        return output_arr
   
        
array = ArrayOperations()
myarray1 = array.createArray()
myarray2 = array.createArray()

mergedArray = array.mergeArray(myarray1,myarray2)


