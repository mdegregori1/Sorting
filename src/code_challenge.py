# Print out each element of the following array on a separate line:


# function that takes in argument 
def separate_line(x):
    for i in (x):
        print(str(i))
# inside of that func, we need a for loop
# inside of that loop, we need to print out the elements

# call function

x = ['Joe', 2, 'Ted', 4.98, 14, 'Sam', 'void *', '42', 'float', 'pointers', 5006]

separate_line(x)