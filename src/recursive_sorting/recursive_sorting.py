# The “divide” part of this algorithm requires us to cut a collection of elements in half until its length is 1. If our collection contains n elements, we will have to perform more halving operations as n grows larger. 


# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # added left + right side elements (to merge)
    elements = len( arrA ) + len( arrB )
    # merged_arr is basically just the result
    merged_arr = [0] * elements

    # track position for arrA by adding pointer a
    # track position for arrB by adding pointer b 
    pointer_a = 0 
    pointer_b = 0 
   
    for x in range(elements):
        if pointer_a >= len(arrA):
            merged_arr[x] = arrB[pointer_b]
            pointer_b += 1
        elif pointer_b >= len(arrB):
            merged_arr[x] = arrA[pointer_a]
            pointer_a += 1
        elif arrA[pointer_a] > arrB[pointer_b]:
            merged_arr[x] = arrB[pointer_b]
            pointer_b += 1
        elif arrB[pointer_b] > arrA[pointer_a]:
            merged_arr[x] = arrA[pointer_a]
            pointer_a += 1
    
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # base case
    if len(arr) <= 1:
        return arr
    # halve elements until all length is one
    middle = len(arr) // 2 
    # left side is array from index 0 to half(middle)
    left = arr[0:middle]
    # right side is array from half(middle) to end of array
    right = arr[middle:len(arr)]
    # merge pairs 
    return merge(merge_sort(left), merge_sort(right))

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

