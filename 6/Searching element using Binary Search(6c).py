def BinarySearch(arr):
    n=len(arr)
    start=0
    end=n-1
    item=int(input("Enter the item to be searched = "))
    while(start<=end):
        mid=int((start+end)/2)
        if arr[mid]==item:
            pos=mid
            print("Element",item,"is found at",pos)
            return pos
        if item<arr[mid]:
            end=mid-1
        else:
            start=mid+1
    print("Element not found")
    return -1

arr=[7,8,9,11,12,15]
print("Array is ",arr)
BinarySearch(arr)
