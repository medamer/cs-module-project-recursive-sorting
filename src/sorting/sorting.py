# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    idxA = 0
    idxB = 0
    idxS = 0
    
    
    while (idxA < len(arrA)) and (idxB < len(arrB)):
        if arrA[idxA] <= arrB[idxB]:
            merged_arr[idxS] = arrA[idxA]
            idxA +=1
        else:
            merged_arr[idxS] = arrB[idxB]
            idxB +=1
        idxS +=1

    while idxA < len(arrA):
        merged_arr[idxS] = arrA[idxA]
        idxA +=1
        idxS +=1
    
    while idxB < len(arrB):
        merged_arr[idxS] = arrB[idxB]
        idxB +=1
        idxS +=1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    n = len(arr)
    if n < 2:
        return
    mid = n // 2
    start = 0
    end = n-1
    left = []
    right = []
    #breakpoint()
    if start < end:
        for i in range(mid):
            left.append(arr[i])

        for j in range(mid, n):
            right.append(arr[j])

    arr = merge(left, right)

    arr = merge_sort(arr)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input

def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
# arr1 = [1, 5, 8, 4, 2]
# arr2 = [9, 6, 0, 3, 7]
# print(merge(arr1, arr2))

arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(arr))