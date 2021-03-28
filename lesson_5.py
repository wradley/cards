# Here is a list. It's very useful
x = [1, 2, 3]

# You can store any type in an array
x = [1, 'hello', False]

# You can even store an array in an array
x = ['hello', True, [1, 2, 3]]

# If you want to get a value out you can 'index' it
print(x[1])

# Usually programming languages start with 0 instead of 1. So if I want to get
# 'hello', I need to use the 0th index
print(x[0])

# I can also keep adding to the list
x.append('a new thing')
print(x[3])

# And I can always get the length of x
print(len(x))


print('\n--- Now you try ---\n')

# Make a 3 by 3 matrix using lists (lists in lists)