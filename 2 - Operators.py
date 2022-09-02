"""
Arithmetic Operators

+ => Addition
- => Subtraction
* => Multiplication
/ => Division
% => Modulus  // Remainder
** => Exponentiation  // power
// => Floor Division // round of to lowest nearest integer

"""

print('Arithmetic Operators')
print('Addition : 10 + 20 = ',10+20)
print('Subtraction : 20 + 10 = ',20+10)
print('Multiplication : 5 * 5 = ',5*5)
print('Division : 50 / 10 = ',50/10)
print('Modulus : 55 % 10 = ',55%10)
print('Exponentiation : 2 ** 4 = ',2**4)
print('Floor Division : 5 // 2 = ',5//2)

print()

print('Comparison Operators')

# > : Greater than operator
print('> : ',20 > 10)

# > : Less than operator
print('< : ',10 < 20)

# == : Equal to => true if both the operands are equal
print('== : ',10==10)

# != : Not equal to => True if both the operands are not equal
print('!= : ',10!=20)

# >= : Greater than or equal to
print('>= : ',10>=9)

# <= : Less than or equal to
print('<= : ',9 <= 10)


print()

print('Logical Operators')

# and => True if both the operands are true
a = 10
b = 20
print('and : ',a==10 and b==20)

# or => True if any one of the operands is true
print('or : ',a==10 or b==10)

# not => True if operand is false
print('not : ',not a==5)

print()

print('Assignment Operators')

#  '=' is for assigining value
n = 10

n += 10 # n = n+10
n -= 10 # n = n-10
n *= 10 # n = n*10
n /= 10 # n = n/10
n %= 10 # n = n%10
n //= 10 # n = n//10
n **= 10 # n = n**10
'''
n &= 10 # n = n&10   // & is Bitwise AND
n |= 10 # n = n|10 // | is Bitwise OR
n ^= 10 # n = n^10 // ^ is Bitwise XOR
n >>= 10 # n = n>>10 // >> is Bitwise Right Shift
n <<= 10 # n = n<<10 // >> is Bitwise Left Shift
'''