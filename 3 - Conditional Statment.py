# If Statement
print('If')
"""
if(condition):  <= if condition return true then it will goes to statement
    statement
"""
a = 10
if(a == 10):
    print('a is 10')

# Note : if there is only one line in statement you can use short hand property
# syntax : if(condition) : statement
if(a == 10) : print('a is 10')


print()

# if else Statement
print('If else')
"""
syntax :
if(condition):    => if condition return false then it goes to else statement
    statement
else:
    statement
"""

if(a < 10):
    print('a is less than 10')
else:
    print('a is greater than or equal to 10')

# Shorthand property for If else
print('a is less than 10') if (a < 10) else print('a is greater than or equal to 10')


print()

# if elif else statement
print('If Elif else')

"""
syntax :
if(condition):
    statement
elif(condition):
    statement
elif(condition):
    statement
      .
      .
      .
else:                <= else is not compulsory
    statement
"""

if(a < 10):
    print('a is less than 10')
elif(a == 10):
    print('a is equal to 10')
else:
    print('a is greater than 10')

print()

# Nested if
print('Nested If')

"""
syntax :
if(condition):
    if(condition):
        if(condition):
"""
if(a < 30):
    if(a < 20):
        if(a <= 10):
            print('a is less than or equal to 10')

print()