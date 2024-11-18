def insertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        temp=arr[i]
        k=i-1
        while(k>=0 and arr[k]>temp):
            arr[k+1]=arr[k]
            k=k-1
        arr[k+1]=temp
    print("Sorted array is = ",arr)
arr=[5,7,2,1,9,0]
insertionSort(arr)
