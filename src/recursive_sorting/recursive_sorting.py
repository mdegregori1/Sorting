# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    #position 0 for both arrays 
    i = 0
    j = 0 
    a = arrA
    b = arrB

    for x in range(elements):
        if i >= len(a):
            merged_arr[x] = b[j]
            j += 1 
        elif j >= len(b):
            merged_arr[x] = a[i]
            i += 1
        elif a[i] < b[j]:
            merged_arr[x] = a[i]
            i += 1
        elif a[i] > b[j]:
            merged_arr[x] = b[j]
            j += 1
            
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # check if the length of the array is less/equal to one 
    if len(arr) <= 1:
        return arr
    else:
        #split the array into halves here by taking the half of the #indeces
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        #merge them at the end
        return merge(left, right)

    return arr



# STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr
