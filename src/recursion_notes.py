# Notes for recursion day

# factorial 4! = 4 * 3 * 2 * 1

# iterative way
# def factorial(n):
#     total = 1
#     for i in range(1, n + 1):
#         total *= i 

#     return total

# recursive
# recurring patterns: 
# 5! = 5 * 4!
# 4! = 4 * 3!
# n! = n * (n-1)!

# def factorial(n):
#     print(n)
#     if n <= 1:
#         return 1
#     return n * factorial(n-1)

# factorial(5)


# Quicksort
# [2, 8, 6, 0, 1, 7, 5, 4, 3, 9]

# pivot = 2
# smaller = [0, 1]
# larger = [8, 6, 7, 5, 4, 3, 9]

# [0,1] + [2] + [8, 6, 7, 5, 4, 3, 9]
# # the above is really #equal to 
# # quicksort(smaller) + [2] + quicksort(larger)
# # becomes 
# return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# quicksort([0,1])
# pivot = 0 
# smaller = []
# larger = [1]

# return quicksort([]) + quicksort([1])
# return [] + [0] + [1]
# becomes 
# [0,1]

# [8, 6, 7, 5, 4, 3, 9]

# pivot = 8
# smaller = [6, 7, 5, 4, 3]
# larger = [9]
# return quicksort([6, 7, 5, 4, 3]) + [8] + [9]

# # becomes
# return [3, 4, 5, 5, 7, 8, 9]

# [6, 7, 5, 4, 3]
# pivot = 6
# smaller = [5, 4, 3]
# larger = [7]

# return quicksort([5,4,3]) + [6] + [7]
# # becomes 
# return [3, 4, 5, 6, 7]

# [5,4,3]
# pivot = 5
# smaller = [4, 3]
# larger = []

# return quicksort([4,3]) + [5] + []
# #bcomes 
# return [3, 4, 5]

# [4,3]
# pivot = 4
# smaller = [3]
# larger = []

# #hit base case
# return [3]  + [4] + []
# # becomes
# return [3, 4]

def quicksort(arr):
    # Base case: arr len 0 or 1 is sorted
    if len(arr) <= 1:
        return arr
    # Pick a pivot
    pivot = arr[0]
    # Separate all vals smaller and larger than pivot
    smaller = []
    larger = []
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            smaller.append(arr[i])
        else:
            larger.append(arr[i])
    # Sort smaller and larger
    # Concatenate smaller + pivot + larger
    return quicksort(smaller) + [pivot] + quicksort(larger)
​
​# chopping in half - idea, usually leds to nlogn