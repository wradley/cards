# Here is that loop wrapped up in a function
def power(x, y):
    result = x
    while y > 1:
        result *= x
        y -= 1
    return result

# This is how you 'call' the function
power(2,2)

# That's pretty useless because we're not saving the value the function
# 'returns'
x = power(2,2)
print(x)

# I can even put the function right inside a print statement
print(power(10,3))

# To create a function, you need to 'define' it
def my_new_function():
    print('I do nothing')

# You can pass stuff to functions. When you write the function (called defining
# the function), you put parameters in the parenthesis
def my_new_function_2(parameter):
    print('here is my parameter: ' + str(parameter))

my_new_function_2('hello')
my_new_function_2(True)
my_new_function_2(3)

# You can also return stuff from a function
def return_the_number_3():
    return 3

three = return_the_number_3()
print(three)

# Functions are useful for several reasons. The first is for reusability. If
# you've got a piece of code that you're writing over and over again in your
# code, you can put it in a function then just call it. The second is that it
# organizes your code without needing comments.

x = [15, 2, 39, 24, 15, 6]
l = x[0]
for v in x:
    if v > l:
        l = v
print(l)

# What does the above code do? I don't know, I need to look at it for a while
# to figure it out...

def find_largest_value(lst):
    l = lst[0]
    for v in lst:
        if v > l:
            l = v
    return l
print(find_largest_value([99,101,8,66,1001,88]))

# Now in my code, when I call find_largest_value([1, 2, 3, 4, 5]), I can easily
# tell what it is doing

print('\n--- Now you try ---\n')

# Write a function that takes in a list and returns a new list that is in the 
# reverse order. Remember list.append(x)
x = [1,2,3,4,5]