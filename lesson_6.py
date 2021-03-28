# When you have lists, loops are very important
x = [1, 2, 3, 4, 5]

# This is a for loop
for value in x:
    print(value)

# You can read it like, "for each value in x"

# You can also just loop a bunch of times
for i in range(5):
    print('this will print 5 times')

# Range just means 0 up to the number you specify. You can do more advanced
# stuff with it but usually it's for this. Read as "for i in the range of 0-4".
# It goes "up to" 5 but not actually 5. So it loops 5 times but starting at
# zero

# There is also a while loop
x = 0
while x < 5:
    print('this will also print 5 times')
    x += 1

# This does the exact same thing as the for loop above but is a little more
# to write out. Sometimes, they're more helpful than a for loop depending on
# the situation.

x = ['another', 'fun', 'array']
while len(x) > 0:
    print(x.pop())


print('\n--- Now you try ---\n')


# Write a loop to calculate x to the power of y and print it out
x = 3
y = 4


# Write a loop to calculate the average of the values in x
x = [2, 5, 99, 101, 42, 8]