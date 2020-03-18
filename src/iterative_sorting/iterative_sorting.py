# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    whole_arr = len(arr)-1
    for i in range(0, whole_arr):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(i+1, len(arr)): 
            if arr[x] < arr[smallest_index]:
                smallest_index = x
        # TO-DO: swap
        # update the current minimum
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        #why is this set up this way?



    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # loop through the length of the array
    whole_arr = len(arr)-1 
    for x in range(0, whole_arr):
    # take 2 indices next to each other
        for y in range(0, whole_arr - x):
            # compare
            if arr[y] > arr[y+1]:
                arr[y], arr[y+1] = arr[y+1], arr[y]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

