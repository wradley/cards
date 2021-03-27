# Let's go over conditionals. It sounds kind of confusing but it just means
# doing something on a condition

x = 3

if x == 3:
    print('x is equal to 3')

if x == 4:
    print('x is equal to 3')

# It kind of reads like english. So since x is 3, only the first print
# statement will happen. The indentation is super important.

x = -100

if x == 3:
    x = 4
    print('now x is 4')
    x = 5
    print('now x is 5')
x = 6
print('now x is 6')

# Lines 18-21 won't run. 22 & 23 still run since they are outside of the if
# 'block'. If something is indented after the 'if' then it is inside the if
# block

# When you use one '=' sign, you are assigning something. Like 'x = 2'. When
# you use the double '==' sign, you are comparing two things. a == b. It will
# always return 'True' or 'False'. In addition to the '==' you can also use
# greater than, greater than or equal to, less than, and less than or equal
# to '>' '>=' '<' '<='
print(5 > 4)
print(4 >= 4)
print(1 < 2)
print(2 <= 2)

# There is also 'not equal to'
print(5 != 4)

# And you don't need to use just numbers
print('tomato' != 'tomahto')

# You can even do something like:
if True:
    print('this will always execute')

if False:
    print('this will never execute')


print('\n--- Now you try ---\n')

# Make 2 if statements. One that will print 'even' if x is even and another
# that will print 'odd' if x is odd. (remember the %)
x = 4