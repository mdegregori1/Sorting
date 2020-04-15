# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    # why (n - 1) ?
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # loop through what is after the current element
        # [4, 3, 1, 2, 6, 5]
        # [1, 3, 4, 2, 6, 5]
        # [1, 2, 4, 3, 6, 5]
        # [1, 2, 3, 4, 6, 5]
        # [1, 2, 3, 4, 5, 6]
        for y in range(smallest_index, len(arr)):
            # compare smallest_index to y 
            if arr[smallest_index] > arr[y]:
                # switch 
                arr[smallest_index], arr[y] = arr[y], arr[smallest_index]

    return arr

# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# selection_sort(arr1)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # loop twice -> 
        # once, starting at index 1 and ending at len 
        # again,starting at index 0 and ending at len - 1 
        # one is behind the other 
        # then compare: if arr[y] > arr[y] + 1, then set + 1 equal to #prev
    for x in range(len(arr)):
        # ask about top loop
        for y in range(0, len(arr) - 1 ):
            # compare here 
            if arr[y] > arr[y + 1]:
                arr[y], arr[y + 1] = arr[y + 1], arr[y]
    
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr