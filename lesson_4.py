# Something that may have helped in the last lesson is the else statement
x = 4

if x % 2 == 0:
    print('even')
else:
    print('odd')

# The else statement has to go after an if. It doesn't make sense on its own.
# If something doesn't evaluate to True, it will end up in the else block

if False:
    print('you will never get here')
else:
    print('this will always run')

# There is one more helpful thing called the 'else if'
x = -1

if x > 0:
    print('positive number')
elif x < 0:
    print('negative number')
else:
    print('x is zero')

# It can be useful when chaining conditions together