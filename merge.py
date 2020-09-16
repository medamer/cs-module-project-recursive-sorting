def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # pre-allocating our output array with the number of elements 
    # we know it will hold at the end 
    merged_arr = [0 for _ in range(elements)]
    
    a = 0
    b = 0
    # Your code here
    # init pointers to the beginning of arrA and arrB
    # compare the elements those pointers are pointing at 
    # whichever element is less than or equal 
    # loop so long as both pointers are in range of their 
    # respective arrays 
    if arrA[a] <= arrB[b]:
        merged_arr.append(arrA[a])
        a += 1
    else:
        merged_arr.append(arrB[b])
        b += 1
            # push that element to the output arr
            # increment the pointer pointing to the element we 
            # just pushed to the output array 

    # now only one of the pointers is in range of its array 
    # in other words, we've moved all of the elements from one 
    # array to the output array, and we need to move all of the 
    # elements of the other array to the output array 


    return merged_arr
	