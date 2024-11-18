def selectionSort(arr):
    n=len(arr)
    for i in range(0,n):
        min=arr[i]
        j=i+1
        for j in range(j,n):
            if min>arr[j]:
                min=arr[j]
                pos=j
                flag=True
        if flag==True:
            temp=arr[pos]
            arr[pos]=arr[i]
            arr[i]=temp
    print("Sorted array is ",arr)
arr=[4,8,7,2,0]
selectionSort(arr)
