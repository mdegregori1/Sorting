def my_recursion(n):
    # print(n)
    if n == 100:
        return 
    else:
        my_recursion(n+1)


my_recursion(1)

#fibonacci

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34

#10th fib number?
#8th fib + 9th fib

#9th fib
#8th fib + 7th fib

#8th fib
# 7th fib + 6th fib

#the base case is...

# 1 and or 0

def recursive_fib(n):
    #base case
    # if n is 0
    if n == 0:
        return 0
    #return 
    # if n is 1 
    if n == 1:
        return 1
    # return 1 

    #if we're not on the base case 
    #recursion n-1 + n-2
    return recursive_fib(n-1) + recursive_fib(n-2)

print(recursive_fib(8))

# quick sort 

[5,9,3,7,2,8,1,6]

# pick the first number 