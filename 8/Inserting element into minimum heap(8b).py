def min_heap(A,i):
    l = left(i)
    r = right(i)
    if l < len(A) and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heap(A, smallest)

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def build_min_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        min_heap(A,k)

A = [3,9,2,1,4,5]
build_min_heap(A)
print("Min heap is",A)
