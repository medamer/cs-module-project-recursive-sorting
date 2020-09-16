# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i 
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        # loop through every elem to the right of the
        # boundary, and keep track of the smallest 
        # elem we've seen so far until we get to the end 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        arr[smallest_index], arr[i] = arr[i], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # keep a flag that tracks whether any swaps occurred 
    swaps_occurred = True 
    while swaps_occurred:
        swaps_occurred = False 
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps_occurred = True

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
# overall runtime: O(n + m) 
# space complexity: O(n + m)
def counting_sort(arr, maximum=None):
    # Your code here
    if len(arr) == 0:
        return arr

    if maximum is None:
        maximum = max(arr)

    buckets = [0 for i in range(maximum+1)]

    # loop through our arr
    # O(n) since we're running through every element in the input array 
    for value in arr:
        if value < 0:
            return "Error, negative numbers not allowed in Count Sort"
        # for each distinct arr value, increment arr[value] by 1 
        buckets[value] += 1

    # at this point, our buckets array has all of the counts of 
    # every distinct value in our input array 
    
    output = []
    # loop through our buckets array 
    # length of buckets can be at most 0..m where m is our m possible value 
    for index, count in enumerate(buckets):
        # for the current count
        output.extend([index for i in range(count)]) 
        # add that many values to an output array 

    return output 
