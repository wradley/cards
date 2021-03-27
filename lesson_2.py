# Here are some really common math things you'll do in python
a = 1
b = 2
c = a + b
d = b / c
e = d * c
f = b - 12345.12345

# Sometimes you'll need to increment a number by one. Or divide it in half.
a = 1
a = a + 1
a = a / 2

# This is a nice shortcut
a = 1
a += 1
a /= 2

# This is called the modulo operator. It's basically just the remainder of a
# division
x = 11 % 10

# 11 divided by 10 is 1 with a remainder of 1. So x = 1
print(x)

# It can be usefull if you're checking whether or not a number is even
number_variable = 3
print(number_variable % 2) # this will be 1 since 3 is an odd number

number_variable = 4
print(number_variable % 2) # this will be 0 since 3 is an odd number